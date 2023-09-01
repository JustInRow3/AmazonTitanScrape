from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'eager' #Webdriver waits until DOMContentLoaded event fire is returned.
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_extension('extension_8_3_0_0.crx')

# Open browser window
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
time.sleep(5)
wd.get('https://www.amazon.com/')
time.sleep(5)

wd.close()