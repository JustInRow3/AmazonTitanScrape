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
# bypass captcha by maximizing window
wd.maximize_window()
wd.get('https://www.amazon.com/') # open amazon
print('Open tab')

print('Maximize tab')
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
time.sleep(2)
wd.find_element(By.CLASS_NAME, 'login').click()
wd.close() # close tab
print('Closed extension tab.')

# Switch to main tab
wd.switch_to.window(original_window)
wd.refresh()
print('Refresh page')
time.sleep(5)

# Input keywords
keyword = 'wool dryer balls'
wd.find_element(By.ID, 'twotabsearchtextbox').send_keys(keyword)
print('Enter Keyword')
wd.find_element(By.ID, 'nav-search-submit-button').click()
print('Click submit')
time.sleep(2)

#select table
#print(table.text.split('\n'))
for i in range(100):
    table = wd.find_element(By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')
    print(i)
    if 'Loading...' in table.text.split('\n'):
        time.sleep(3)
    else:
        print(table.text)
        break

time.sleep(1)

wd.close()
wd.quit()
