from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'none'
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Open browser window
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wd.implicitly_wait(5)
wd.get('https://www.amazon.com/')

time.sleep(10)
wd.close()
