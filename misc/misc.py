import pandas as pd
import time
import os
from selenium.webdriver.support import expected_conditions as EC


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


def iterate_keyword(file, wait, writer, wd, columns):
    from selenium.webdriver.common.by import By
    for_save = pd.DataFrame()
    wd.implicitly_wait(30)
    for keyword in read_xlsx(file):
        # Input keywords
        #keyword = 'wool dryer balls'
        excel_out = pd.ExcelWriter(writer)
        wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))).clear()
        print('Clear input field.')
        wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))).send_keys(keyword)
        print('Enter Keyword')
        wait.until(EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))).click()
        print('Click submit')

        # select table then wait until extension is done
        wait.until(EC.presence_of_element_located((By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')))

        for i in range(30):
            time.sleep(3)
            table = wd.find_element(By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')
            print('Loop: ' + str(i))
            try:
                if 'Loading...' in table.text.split('\n'):
                    if i == 10 or i == 20:  # refresh page if took too much time for results
                        #wd.refresh()
                        wait.until(EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))).click()
                        time.sleep(3)
                        wait.until(
                            EC.presence_of_element_located((By.ID, 'amazon-analysis-eefljgmhgaidffapnppcmmafobefjece')))
                        print('Click submit')
                else:
                    # print(table.text.split('\n'))
                    time.sleep(3)
                    excel = table.text.split('\n')
                    data = [element for element in excel if (if_number_(element))]
                    data.insert(0, keyword)
                    # Transpose first before append
                    for_transpose = pd.DataFrame(data, dtype=str).transpose()
                    for_transpose.columns=columns
                    for_save = pd.concat([for_save, for_transpose], ignore_index=True)
                    print(for_save)
                    print('Write to dataframe.')
                    break
            except:
                print('Timeout encountered!')
                pass
    #write to excel file
    for_save.to_excel(excel_out)
    excel_out.close()
