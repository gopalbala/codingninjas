import csv
with open('amazon_jobs_dataset.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    filedata = list(reader)
    monthwise = {}
    for row in filedata:
        if 'January' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('January') != None:
                monthwise['January'] = monthwise['January'] + 1
            else:
                monthwise['January'] = 1
        
        if 'February' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('February') != None:
                monthwise['February'] = monthwise['February'] + 1
            else:
                monthwise['February'] = 1
        
        if 'March' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('March') != None:
                monthwise['March'] = monthwise['March'] + 1
            else:
                monthwise['March'] = 1
                
        if 'April' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('April') != None:
                monthwise['April'] = monthwise['April'] + 1
            else:
                monthwise['April'] = 1
        
        if 'May' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('May') != None:
                monthwise['May'] = monthwise['May'] + 1
            else:
                monthwise['May'] = 1
        
        if 'June' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('June') != None:
                monthwise['June'] = monthwise['June'] + 1
            else:
                monthwise['June'] = 1
        
        if 'July' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('July') != None:
                monthwise['July'] = monthwise['July'] + 1
            else:
                monthwise['July'] = 1
        
        if 'August' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('August') != None:
                monthwise['August'] = monthwise['August'] + 1
            else:
                monthwise['August'] = 1
                
        if 'September' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('September') != None:
                monthwise['September'] = monthwise['September'] + 1
            else:
                monthwise['September'] = 1
        
        if 'October' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('October') != None:
                monthwise['October'] = monthwise['October'] + 1
            else:
                monthwise['October'] = 1
        
        if 'November' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('November') != None:
                monthwise['November'] = monthwise['November'] + 1
            else:
                monthwise['November'] = 1
        
        if 'December' in row['Posting_date'] and '2018' in row['Posting_date']:
            if monthwise.get('December') != None:
                monthwise['December'] = monthwise['December'] + 1
            else:
                monthwise['December'] = 1
                
    for key in monthwise.keys():
        print(key,monthwise[key])
    # print('January '+str(monthwise['January']))
    # print('February '+str(monthwise['February']))
    # print('March '+str(monthwise['March']))
    # print('April '+str(monthwise['April']))
    # print('May '+str(monthwise['May']))
    # print('June '+str(monthwise['June']))
    # print('July '+str(monthwise['July']))
    # print('August '+str(monthwise['August']))
    # print('September '+str(monthwise['September']))
    # print('October '+str(monthwise['October']))
    # print('November '+str(monthwise['November']))
    # print('December '+str(monthwise['December']))