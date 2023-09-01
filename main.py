from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'eager' # Webdriver waits until DOMContentLoaded event fire is returned.
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_extension('extension_8_3_0_0.crx')

# Open browser window
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wd.get('https://www.amazon.com/') # open amazon
# bypass captcha by maximizing window
wd.maximize_window()
wait = WebDriverWait(wd, 10) # setup wait
original_window = wd.current_window_handle # store the ID of the original window

# Switch to other tab
for tab in wd.window_handles:
    if tab != original_window:
        wd.switch_to.window(tab)
        print('Switched to other tab to login: ' + wd.title)
        break

# Input username and pw then click login
# id="username"
# id = "password"
wd.find_element(By.ID, 'username').send_keys('karfafton@gmail.com')
wd.find_element(By.ID, 'password').send_keys('@Dummy123')
wd.find_element(By.CLASS_NAME, 'login').click()
wd.close() # close tab

# Switch to main tab
wd.switch_to.window(original_window)
wd.refresh()

# Input keywords
#id="twotabsearchtextbox"
keyword = 'wool dryer balls'
wd.find_element(By.ID, 'twotabsearchtextbox').send_keys(keyword)

time.sleep(5)

wd.close()
wd.quit()
