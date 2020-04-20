import csv
import random
from docxtpl import DocxTemplate
doc = DocxTemplate("example.docx")

SPR_RUB = ""
SPR_KOP = ""

num2words = {1: 'ОДИН', 2: 'ДВА', 3: 'ТРИ', 4: 'ЧЕТЫРЕ', 5: 'ПЯТЬ', \
            6: 'ШЕСТЬ', 7: 'СЕМЬ', 8: 'ВОСЕМЬ', 9: 'ДЕВЯТЬ', 10: 'ДЕСЯТЬ', \
            11: 'ОДИННАДЦАТЬ', 12: 'ДВЕНАДЦАТЬ', 13: 'ТРИНАДЦАТЬ', 14: 'ЧЕТЫРНАДЦАТЬ', \
            15: 'ПЯТНАДЦАТЬ', 16: 'ШЕСТНАДЦАТЬ', 17: 'СЕМНАДЦАТЬ', 18: 'ВОСЕМНАДЦАТЬ',
            19: 'ДЕВЯТНАДЦАТЬ', 20:'ДВАДЦАТЬ', 30:'ТРИДЦАТЬ', 40:'СОРОК', 50:'ПЯТДЕСЯТ',
            60: 'ШЕСТЬДЕСЯТ', 70:'СЕМЬДЕСЯТ', 80:'ВОСЕМЬДЕСЯТ', 90:'ДЕВЯНОСТО', 100:'СТО',
            200: 'ДВЕСТИ', 300: 'ТРИСТА', 400: 'ЧЕТЫРЕСТА', 500: 'ПЯТЬСОТ', 600: 'ШЕСТЬСОТ',
            700: 'СЕМЬСОТ', 800: 'ВОСЕМЬСОТ', 900: 'ДЕВЯТЬСОТ'}

num2words_k = {1: 'ОДНА', 2: 'ДВЕ', 3: 'ТРИ', 4: 'ЧЕТЫРЕ', 5: 'ПЯТЬ', \
            6: 'ШЕСТЬ', 7: 'СЕМЬ', 8: 'ВОСЕМЬ', 9: 'ДЕВЯТЬ', 10: 'ДЕСЯТЬ', \
            11: 'ОДИННАДЦАТЬ', 12: 'ДВЕНАДЦАТЬ', 13: 'ТРИНАДЦАТЬ', 14: 'ЧЕТЫРНАДЦАТЬ', \
            15: 'ПЯТНАДЦАТЬ', 16: 'ШЕСТНАДЦАТЬ', 17: 'СЕМНАДЦАТЬ', 18: 'ВОСЕМНАДЦАТЬ',
            19: 'ДЕВЯТНАДЦАТЬ', 20:'ДВАДЦАТЬ', 30:'ТРИДЦАТЬ', 40:'СОРОК', 50:'ПЯТДЕСЯТ',
            60: 'ШЕСТЬДЕСЯТ', 70:'СЕМЬДЕСЯТ', 80:'ВОСЕМЬДЕСЯТ', 90:'ДЕВЯНОСТО', 100:'СТО',
            200: 'ДВЕСТИ', 300: 'ТРИСТА', 400: 'ЧЕТЫРЕСТА', 500: 'ПЯТЬСОТ', 600: 'ШЕСТЬСОТ',
            700: 'СЕМЬСОТ', 800: 'ВОСЕМЬСОТ', 900: 'ДЕВЯТЬСОТ'}

BANK = "АО \"Банкрот Банк\" Г. НАБЕРЕЖНЫЕ ЧЕЛТЫ"
COMP = "ООО \"СВЯЗЬ FINGER-STICK\""

BIK = random.randint(100000000, 999999999)
print("generated BIK: ", BIK)

INN = random.randint(1000000000, 9999999999)
print("generated INN: ", INN)

KPP = random.randint(100000000, 999999999)
print("generated KPP: ", KPP)

ACC_1 = '3010' + str(random.randint(10000, 99999)) + '0000000' + str(random.randint(1000, 9999))
print("generated ACC_1: ", ACC_1)

ACC_2 = '4070' + str(random.randint(10000, 99999)) + '0000000' + str(random.randint(1000, 9999))
print("generated ACC_2: ", ACC_2)

ACC_3 = random.randint(1, 99999)
print("generated ACC_3: ", ACC_3)

DAY = random.randint(1, 30)
print("generated DAY: ", DAY)

MONTH = random.randint(1, 12)
print("generated MONTH: ", MONTH)

YEAR = random.randint(0, 20)
if YEAR < 10:
    YEAR = '0' + str(YEAR)
print("generated YEAR: ", YEAR)

INDEX = random.randint(100000, 999999)
INDEXE = random.randint(100000, 999999)

INNE = random.randint(1000000000, 9999999999)
print("generated INNE: ", INNE)

KPPE = random.randint(100000000, 999999999)
print("generated KPPE: ", KPPE)

EXECUTOR = "ООО \"СВЯЗЬ FINGER-STICK\", ИНН " + str(INN) + ", КПП " + str(KPP) + ", " + str(INDEX) + ", Сладководск г, Неплохая ул, дом 5"
EMPLOYER = "ООО \"ОТДЫХ\", ИНН " + str(INNE) + ", КПП " + str(KPPE) + ", " + str(INDEXE) + ", Омск г, Такая Себе ул, дом 6"
FOUNDING = str(random.randint(10000000, 99999999)) + " от " + str(random.randint(1, 30)) + "." + str(random.randint(1, 12)) + "." + str(random.randint(1970, 2020))

JOB_1 = "ИСХОДЯЩИЕ ЗВОНКИ"
JOB_2 = "ВХОДЯЩИЕ ЗВОНКИ"
JOB_3 = "СМС"
JOB_4 = "ИНТЕРНЕТ"

#_lab1_#

data_file_1 = "D:\DEV\mobile\lab3\data\data1.csv"

sms_sum = 0  
out_calls_sum = 0
inc_calls_sum = 0

number = '915642913'
sms_tariff = 1
#first 5 for free
out_calls_tariff = 1
inc_calls_tariff = 1

# initializing the titles and rows
fields = [] 
rows = [] 
  
# reading csv file 
with open(data_file_1, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader)
    
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    #print("Total no. of lines in a CDR file: %d"%(csvreader.line_num)) 
  
    # calculating SMS tariffication
    for row in rows[:csvreader.line_num]: 
        if number in row[1]:
            sms_sum += float(row[4])
    sms_price = sms_sum*sms_tariff-5
    if sms_price < 0:
        sms_price = 0
    #print(sms_price, "rubles for SMS")

    # calculating outgoing calls tariffication
    for row in rows[:10]: 
        if number in row[1]:
            out_calls_sum += float(row[3])
    out_calls_price = out_calls_sum*out_calls_tariff
    if out_calls_price < 0:
        out_calls_price = 0
    #print(out_calls_price, "rubles for outgoing calls")

    # calculating incoming calls tariffication
    for row in rows[:10]: 
        if number in row[2]:
            inc_calls_sum += float(row[3])
    inc_calls_price = inc_calls_sum*inc_calls_tariff
    if inc_calls_price < 0:
        inc_calls_price = 0
    #print(inc_calls_price, "rubles for incoming calls")

    # total price
    total_price = sms_price+out_calls_price+inc_calls_price
    #print("total price is:", total_price)

#_lab2_#
    
total_traffic = 0
total_occurences = 0
i = 0
data_file_2 = "D:\DEV\mobile\lab3\data\data2.csv"
#file = input("Enter path to CDR file: ")

#number = input("Enter IP address: ")
ip_number = "192.168.250.59"
#first 1000#b for free
tariff = 1

# initializing the titles and rows
fields_2 = [] 
rows_2 = [] 
rowlist = []
traflist = []
# reading csv file 
with open(data_file_2, 'r') as csvfile_2: 
    # creating a csv reader object 
    csvreader_2 = csv.reader(csvfile_2) 
      
    # extracting field names through first row 
    fields_2 = next(csvreader_2)
    
    # extracting each data row one by one 
    for row in csvreader_2: 
        rows_2.append(row) 
  
    # get total number of rows 
    #print("Total no. of lines in a CDR file: %d"%(csvreader.line_num)) 
  
    #
    # calculating incoming calls tariffication
    for row in rows_2[1:17450]:
        if row[3] == ip_number:
            total_traffic = total_traffic + int(row[12])
            total_occurences = total_occurences + 1
            #print(int(row[12]))
            traflist += {(row[1], row[12])}
        if row[4] == ip_number:
            total_traffic = total_traffic + int(row[12])
            total_occurences = total_occurences + 1
            traflist += {(row[1], row[12])}
    c = ""
    # total price
    if total_traffic < 1000:
        c = "байт"
        total_cost = (total_traffic*1000-1000)*1/1000000000
        if total_cost < 0:
            total_cost = 0
    if 1000000 > total_traffic > 1000:
        total_traffic = total_traffic/1000
        c = "КБ"
        total_cost = (total_traffic*1000-1000)*1/1000000
        if total_cost < 0:
            total_cost = 0
    if 1000000000 > total_traffic > 1000000:
        total_traffic = total_traffic/1000000
        c = "МБ"
        total_cost = (total_traffic-1)*1
        if total_cost < 0:
            total_cost = 0
    #print("total traffic:", total_traffic, c)
    #print("total occurences:", total_occurences)
    #print("total cost: ", round(total_cost, 2), "rubles")
    
def cringe(N):
    try:
        print(num2words[N])
    except KeyError:
        try:
            sotkas = num2words[N-N%100]
            tens = num2words[N%100-N%10]
            odins = num2words[N%10]
            if 9 < (N%100) < 20:
                odins = ''
                tens = num2words[N%100]
            #print(sotkas + " " + tens + " " + odins)
            return(sotkas + " " + tens + " " + odins)
        except KeyError:
            print('Number out of range')
            
def kringe(N):
    try:
        print(num2words_k[N])
    except KeyError:
        try:
            tens = num2words_k[N%100-N%10]
            odins = num2words_k[N%10]
            if 9 < (N%100) < 20:
                odins = ''
                tens = num2words_k[N%100]
            #print(tens + " " + odins)
            return(tens + " " + odins)
        except KeyError:
            print('Number out of range')

TOTAL = (out_calls_price+inc_calls_price+sms_price+round(total_cost, 2))

pogs = round(TOTAL%1, 2)*100
if 4 < pogs%10 < 10:
    SPR_KOP = "КОПЕЕК"
elif pogs%10 == 1:
    SPR_KOP = "КОПЕЙКА"
elif pogs%10 == 0:
    SPR_KOP = "КОПЕЕК"
elif 1 < pogs%10 < 5:
    SPR_KOP = "КОПЕЙКИ"
if pogs-pogs%10 == 10:
    SPR_KOP = "КОПЕЕК"
#

rpogs = int(TOTAL)%10
if 4 < rpogs%10 < 10:
    SPR_RUB = "РУБЛЕЙ"
elif rpogs%10 == 1:
    SPR_RUB = "РУБЛЬ"
elif rpogs%10 == 0:
    SPR_RUB = "РУБЛЕЙ"
elif 1 < rpogs%10 < 5:
    SPR_RUB = "РУБЛЯ"
if int(TOTAL)%100-rpogs == 10:
    SPR_RUB = "РУБЛЕЙ"

TOTAL_K = round(TOTAL%1, 2)
TOTAL_K = TOTAL_K*100
TOTAL_K = kringe(int(TOTAL_K))

context = { 'BANK' : BANK, 'BIK' : BIK, 'COMP' : COMP, 'INN' : INN, 'KPP' : KPP, 'ACC_1' : ACC_1, 'ACC_2' : ACC_2,
            'ACC_3' : ACC_3, 'DAY' : DAY, 'MONTH' : MONTH, 'YEAR' : YEAR, 'EXECUTOR' : EXECUTOR, 'EMPLOYER' : EMPLOYER,
            'FOUNDING' : FOUNDING, 'JOB_1' : JOB_1, 'JOB_2' : JOB_2, 'JOB_3' : JOB_3, 'JOB_4' : JOB_4, 'AM_1' : out_calls_sum,
            'C_1' : "мин", 'P_1' : out_calls_tariff, 'S_1' : out_calls_price, 'AM_2' : inc_calls_sum, 'C_2' : "мин",
            'P_2' : inc_calls_tariff, 'S_2' : inc_calls_price, 'AM_3' : sms_sum,'C_3' : "шт", 'P_3' : sms_tariff,
            'S_3' : sms_price, 'AM_4' : round(total_traffic, 2), 'C_4' : c, 'P_4' : '1', 'S_4' : round(total_cost, 2),
            'TOTAL' : TOTAL, 'NDS' : round(TOTAL/5, 2), 'TOTAL_TEXT_RUB' : cringe(int(TOTAL)), 'TOTAL_TEXT_KOP' : TOTAL_K,
            'SPR_KOP' : SPR_KOP, 'SPR_RUB' : SPR_RUB,  'BOSS' : "Важный Х.З.", 'BUHGALTER' : "Маркелова Е.А."}
doc.render(context)
doc.save("example_final.docx")

print("Starting conversion.... ")

from docx2pdf import convert
####  Edit this to edit output file location
convert("D:\DEV\mobile\lab3\example_final.docx")

print("pdf ready!")
