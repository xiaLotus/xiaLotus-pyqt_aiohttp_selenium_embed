import sys
# 更換
package_path = r".\python-3.11.1\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import asyncio
import time
import aiohttp


# Step 1: Create a background thread to run the Selenium task
class SeleniumThread(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.driver = None

    def run(self):
        # Initialize WebDriver (Edge in this case)
        service = Service('msedgedriver.exe')
        self.driver = webdriver.Edge(service=service)
        
        # Step 2: Open Google and update GUI
        self.driver.get('https://www.google.com')
        self.result_signal.emit("Google 頁面已打開")
        
        # Step 3: Find the search box and input '123'
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys('123')
        self.result_signal.emit("已輸入 '123'")
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for search results to load

        # Step 4: Get the page title and send it back to the GUI
        page_title = self.driver.title
        self.result_signal.emit(f"搜尋結果頁面標題: {page_title}")

        time.sleep(3)  # Wait for 3 seconds before closing the browser
        self.driver.quit()  # Close the browser

# Step 5: Create the PyQt5 GUI
class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selenium + PyQt5 Example")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("程式正在運行...", self)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        # Step 6: Create the Selenium background thread and start it immediately
        self.selenium_thread = SeleniumThread()
        self.selenium_thread.result_signal.connect(self.update_label)

        # Start the thread when the program runs
        self.selenium_thread.start()

    def update_label(self, result):
        # Update the label with the result from the Selenium task
        self.label.setText(result)

# Step 7: Run the PyQt5 application
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()