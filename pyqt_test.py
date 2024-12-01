import sys
# 更換
package_path = r".\python-3.11.3\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QTextEdit
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
import thread
import schedule

with open('sheet.txt', 'r', encoding='utf-8') as file:
    mysheet = file.read()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("暫時測試用")

        self.setStyleSheet(mysheet)

        self.setFixedSize(600, 400)

        self.admin = QLineEdit(self)
        self.admin.setPlaceholderText("帳號： ")

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("密碼： ")
        self.password.setEchoMode(QLineEdit.Password) 

        self.submit_button = QPushButton("啟動", self)

        
        # 創建一個文本區域用來顯示日志
        self.log_display = QTextEdit(self)
        self.log_display.setReadOnly(True)  # 設為只讀模式，防止用戶編輯

        # 連接按鈕點擊事件
        self.submit_button.clicked.connect(self.on_submit)
        
        # 按下 password 那處的 enter 可以過
        self.password.returnPressed.connect(self.on_submit)


        # 創建佈局
        layout = QVBoxLayout()
        layout.addWidget(self.admin)
        layout.addWidget(self.password)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.log_display)
        
        # 設定佈局
        self.setLayout(layout)

    def on_submit(self):
        # 獲取輸入框中的文本
        text1 = self.admin.text()
        text2 = self.password.text()

        # 在日志區域中顯示
        log_message = f"輸入1: {text1}\n輸入2: {text2}\n"
        self.log_display.append(log_message)
        
        self.limit_log_lines()

        # 清空輸入框
        self.admin.clear()
        self.password.clear()

        self.submit_button.setEnabled(False)
    
    def limit_log_lines(self):
        log_text = self.log_display.toPlainText()

        log_lines = log_text.split('\n')

        if len(log_lines) > 10:
            log_lines = log_lines[-10: ]

            self.log_display.setPlainText('\n'.join(log_lines))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())