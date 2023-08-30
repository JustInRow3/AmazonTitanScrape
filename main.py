from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'none'
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_extension('./extension_8_3_0_0.crx')

# Open browser window
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
time.sleep(5)
wd.get('https://www.amazon.com/')
time.sleep(10)

"""from amazoncaptcha import AmazonCaptcha
captcha = AmazonCaptcha.fromdriver(wd)
solution = 'Not solved'
count = 0"""
"""if solution != 'Not solved' or count != 10:
    solution = captcha.solve(keep_logs=True)
    print(solution)
    count += 1
#captcha_image = wd.find_element(By.XPATH, 
'/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img').get_attribute('src')
#print(captcha_image)"""
