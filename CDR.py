import csv

#filename = "D:\DEV\mobile\lab1\data.csv"
file = input("Enter path to CDR file: ")

sms_sum = 0  
out_calls_sum = 0
inc_calls_sum = 0

#number = 915642913
number = input("Enter phone number: ")
sms_tariff = 1
#first 5 for free
out_calls_tariff = 1
inc_calls_tariff = 1

# initializing the titles and rows
fields = [] 
rows = [] 
  
# reading csv file 
with open(file, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader)
    
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of lines in a CDR file: %d"%(csvreader.line_num)) 
  
    # calculating SMS tariffication
    for row in rows[:csvreader.line_num]: 
        if number in row[1]:
            sms_sum += float(row[4])
    sms_price = sms_sum*sms_tariff-5
    if sms_price < 0:
        sms_price = 0
    print(sms_price, "rubles for SMS")

    # calculating outgoing calls tariffication
    for row in rows[:10]: 
        if number in row[1]:
            out_calls_sum += float(row[3])
    out_calls_price = out_calls_sum*out_calls_tariff
    if out_calls_price < 0:
        out_calls_price = 0
    print(out_calls_price, "rubles for outgoing calls")

    # calculating incoming calls tariffication
    for row in rows[:10]: 
        if number in row[2]:
            inc_calls_sum += float(row[3])
    inc_calls_price = inc_calls_sum*inc_calls_tariff
    if inc_calls_price < 0:
        inc_calls_price = 0
    print(inc_calls_price, "rubles for incoming calls")

    # total price
    total_price = sms_price+out_calls_price+inc_calls_price
    print("total price is:", total_price)
