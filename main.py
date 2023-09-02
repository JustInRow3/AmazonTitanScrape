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

print(wd.title)

#Check for captcha 3 times
for i in range(3):
    if wd.title == 'Amazon.com. Spend less. Smile more.':
        print('No captcha encountered.')
        break
    else:
        time.sleep(1)
        wd.quit()
        wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        time.sleep(3)
        print('Reopen another window!')
        wd.get('https://www.amazon.com/')  # open amazon
        wd.maximize_window()
        wd.refresh()
        time.sleep(3)
    print('Captcha encountered 3 times! Exited script, please rerun!')
    quit()

original_window = wd.current_window_handle # store the ID of the original window
wait = WebDriverWait(wd, 50) # setup wait

# Switch to other tab
for tab in wd.window_handles:
    if tab != original_window:
        wd.switch_to.window(tab)
        print('Switched to other tab to login: ' + wd.title)
        break

# Input username and pw then click login
wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys('karfafton@gmail.com')
wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys('@Dummy123')
wd.find_element(By.CLASS_NAME, 'login').click()
time.sleep(2)
wd.close() # close tab
print('Delay 2 secs before close extension tab.')

# Switch to main tab
wd.switch_to.window(original_window)
wd.refresh()
print('Refresh page')
time.sleep(2)

# Input keywords
keyword = 'wool dryer balls'
wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))).send_keys(keyword)
print('Enter Keyword')
wait.until(EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))).click()
print('Click submit')

#select table then wait until extension is done
wait.until(EC.presence_of_element_located((By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')))
for i in range(100):
    time.sleep(3)
    table = wd.find_element(By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')
    print('Loop: ' + str(i))
    if 'Loading...' in table.text.split('\n'):
        if i == 30: # refresh page if took too much time for results
            wd.refresh()
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')))
    else:
        print(table.text.split('\n'))
        excel = table.text.split('\n')
        break

wd.close()
wd.quit()
