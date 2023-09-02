filename = '9_2_2023.xlsx'
import pandas as pd
import os


"""rel_path = "../For_Run/" + filename
abs_file_path = os.path.join(script_dir, rel_path)"""

def file_(file):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "../For_Run/" + file
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path
#print(file(filename))
def read_xlsx(file):
    data = pd.read_excel(file_(file))
    print(data['Keyword'])
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

#print(if_number('0.0'))