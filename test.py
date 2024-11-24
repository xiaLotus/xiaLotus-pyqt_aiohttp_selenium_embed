import sys
# 更換
package_path = r".\python-3.11.1\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('msedgedriver.exe')
driver = webdriver.Edge(service = service)
import time

driver.get('https://www.google.com')
time.sleep(1)  # 等待 5 秒
print(driver.title)

# 找到搜尋框
search_box = driver.find_element(By.NAME, 'q')

# 在搜尋框中輸入 "123"
search_box.send_keys('123')

# 提交搜尋
search_box.send_keys(Keys.RETURN)

input("按 Enter 鍵關閉瀏覽器...")
driver.quit()