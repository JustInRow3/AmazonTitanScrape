from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import sys
import pandas as pd
sys.path.append("..")
from misc import misc

#Constant filepath of input xlsx file
filetorun = '9_2_2023'
filetorun_excel = filetorun + '.xlsx'
write_excel_path = misc.write_excel_path(filetorun)
print(write_excel_path)

def if_number_(string):
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']
    return all([(x in int_list) for x in string])

options = Options()
options.page_load_strategy = 'eager' # Webdriver waits until DOMContentLoaded event fire is returned.
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_extension('extension_8_3_0_0.crx')
service = Service(executable_path=r'C:\Users\jjie\.wdm\drivers\chromedriver\win64\116.0.5845.141\chromedriver-win32\chromedriver.exe')

# Open browser window
wd = webdriver.Chrome(service=service, options=options)
wd.implicitly_wait(10)

# bypass captcha by maximizing window
wd.maximize_window()
wd.get('https://www.amazon.com/') # open amazon
print('Open tab')
print('Maximize tab')

print(wd.title)

#Check for captcha 3 times
for i in range(4):
    print('Times tab opened: ' + str(i))
    if wd.title == 'Amazon.com. Spend less. Smile more.':
        print('No captcha encountered.')
        break
    elif i == 3:
        print('Please rerun script, error encountered in captcha!')
        break
        quit()
    else:
        wd.quit()
        wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wd.implicitly_wait(10)
        time.sleep(3)
        print('Reopen another window!')
        wd.get('https://www.amazon.com/')  # open amazon
        wd.maximize_window()
        wd.refresh()
        time.sleep(3)

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
"""for_write = pd.DataFrame(columns=['Keyword', 'Total Results', 'On First Page', 'Ind. Published', 'Average_BSR',
                                  'Low_BSR', 'High_BSR', 'Average_Reviews', 'Low_Reviews', 'High_Reviews',
                                  'Average_Price', 'Low_Price', 'High_Price', 'Demand'])
col = ['Keyword', 'Total Results', 'On First Page', 'Ind. Published', 'Average_BSR',
                                  'Low_BSR', 'High_BSR', 'Average_Reviews', 'Low_Reviews', 'High_Reviews',
                                  'Average_Price', 'Low_Price', 'High_Price', 'Demand']"""

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
    table_details = table.text
    print('Loop: ' + str(i))
    if 'Loading...' in table_details.split('\n'):
        if i == 30: # refresh page if took too much time for results
            wd.refresh()
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')))
    else:
        #print(table.text.split('\n'))
        excel = table.text.split('\n')
        data = [element for element in excel if (if_number_(element))]
        data.insert(0, keyword)
        #Transpose first before append
        for_transpose = pd.DataFrame(data, dtype=str).transpose()
        #write to excel file
        for_transpose.to_excel(write_excel_path)
        break


wd.close()
wd.quit()
