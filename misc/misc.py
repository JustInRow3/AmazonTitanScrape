import pandas as pd
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def file_(file):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "../For_Run/" + file
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path
def write_excel_path(file):
    filename_date = time.strftime("_%Y%m%d%H%M%S", time.localtime())
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "../Done_Run/" + file + filename_date + '.xlsx'
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path
#print(file(filename))
def read_xlsx(file):
    data = pd.read_excel(file_(file))
    #print(data['Keyword'])
    return data['Keyword']
#read_xlsx(filename)
list = ['Titans Quick View Results', 'Total Results', '335', 'On First Page', '60',
        'Ind. Published', '0', 'Best Seller Rank', 'Average', '57,806', 'Low', '0',
        'High', '329,223', 'Reviews', 'Average', '6,484', 'Low', '0', 'High', '71,518',
        'Price', 'Average', '0.00', 'Low', '0.00', 'High', '0.00', 'Links', 'Sell Books on Amazon',
        'Join Facebook Group', 'Download 1st Page Data', 'NEW - Get Titans Pro', 'Opportunity', '?',
        'Demand', '7', '?', 'To see analysis - Upgrade to Titans Pro']

def if_number_(string):
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']
    return all([(x in int_list) for x in string])

def if_number_(string):
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']
    return all([(x in int_list) for x in string])

#print(if_number('0.0'))


def iterate_keyword(file, wait, wd, writer):
    from selenium.webdriver.common.by import By
    for keyword in read_xlsx(file):
        # Input keywords
        #keyword = 'wool dryer balls'
        wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))).clear()
        print('Clear input field.')
        wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))).send_keys(keyword)
        print('Enter Keyword')
        wait.until(EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))).click()
        print('Click submit')

        # select table then wait until extension is done
        wait.until(EC.presence_of_element_located((By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')))

        for i in range(100):
            time.sleep(3)
            table = wd.find_element(By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')
            print('Loop: ' + str(i))
            if 'Loading...' in table.text.split('\n'):
                if i == 30:  # refresh page if took too much time for results
                    wd.refresh()
                    time.sleep(5)
                    wait.until(
                        EC.presence_of_element_located((By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')))
            else:
                # print(table.text.split('\n'))
                excel = table.text.split('\n')
                data = [element for element in excel if (if_number_(element))]
                data.insert(0, keyword)
                # Transpose first before append
                for_transpose = pd.DataFrame(data, dtype=str).transpose()
                # write to excel file
                startrow = writer.sheets['Niche'].max_row
                for_transpose.to_excel(writer, Header=False, startrow=startrow, sheet_name='Niche')
                print('Write to excel.')
                break
