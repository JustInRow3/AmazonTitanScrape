import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("..")
from misc import misc

columns = ['Keyword', 'Total Results', 'On First Page', 'Ind. Published', 'Average_BSR',
                                  'Low_BSR', 'High_BSR', 'Average_Reviews', 'Low_Reviews', 'High_Reviews',
                                  'Average_Price', 'Low_Price', 'High_Price', 'Demand']

#Constant filepath of input xlsx file
filetorun = '9_2_2023' # Filename of excel input inside For_Run folder
filetorun_excel = filetorun + '.xlsx'
write_excel_path = misc.write_excel_path(filetorun)
print(write_excel_path)

# Create new excel file every run
wb = openpyxl.Workbook()
ws = wb.active
wb.save(write_excel_path)
wb.close()
time.sleep(2)

print('Create excel file output: ' + write_excel_path)
options = Options()
options.page_load_strategy = 'eager' # Webdriver waits until DOMContentLoaded event fire is returned.
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_extension('extension_8_3_0_0.crx')
service = Service(executable_path=r'C:\Users\jjie\.wdm\drivers\chromedriver\win64\116.0.5845.180\chromedriver-win32\chromedriver.exe')
#service=Service(ChromeDriverManager().install())

# Open browser window
wd = webdriver.Chrome(service=service, options=options)
wd.implicitly_wait(10)

# bypass captcha by maximizing window
wd.maximize_window()
time.sleep(3)
wd.get('https://www.amazon.com/') # open amazon
time.sleep(3)
print('Open tab')
print('Maximize tab')

print(wd.title)

#Check for captcha 3 times
for i in range(6):
    print('Times tab opened: ' + str(i))
    if wd.title == 'Amazon.com. Spend less. Smile more.':
        print('No captcha encountered.')
        break
        """ elif i == 3:
        print('Please rerun script, error encountered in captcha!')
        break
        quit()"""
    else:
        wd.quit()
        options = Options()
        options.page_load_strategy = 'eager'  # Webdriver waits until DOMContentLoaded event fire is returned.
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_extension('extension_8_3_0_0.crx')
        service = Service(executable_path=r'C:\Users\jjie\.wdm\drivers\chromedriver\win64\116.0.5845.180\chromedriver-win32\chromedriver.exe')
        #service = Service(ChromeDriverManager().install())
        # Open browser window
        wd = webdriver.Chrome(service=service, options=options)
        wd.implicitly_wait(10)
        print('Reopen another window!')
        wd.get('https://www.amazon.com/')  # open amazon
        time.sleep(3)
        wd.maximize_window()
        wd.refresh()

original_window = wd.current_window_handle # store the ID of the original window
wait = WebDriverWait(wd, 50) # setup wait

# Switch to other tab
for tab in wd.window_handles:
    if tab != original_window:
        wd.switch_to.window(tab)
        print('Switched to other tab to login: ' + wd.title)
        break

# Input username and pw then click login
wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys('*******')
time.sleep(1)
wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys('*******')
time.sleep(1)
wd.find_element(By.CLASS_NAME, 'login').click()
time.sleep(2)
wd.close() # close tab
print('Delay 2 secs before close extension tab.')

# Switch to main tab
wd.switch_to.window(original_window)
wd.refresh()
print('Refresh page')
time.sleep(2)

misc.iterate_keyword(file=filetorun_excel, writer=write_excel_path, wait=wait, wd=wd, columns=columns)

wd.quit()
