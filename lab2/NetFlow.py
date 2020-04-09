import csv
import matplotlib.pyplot as plt
total_traffic = 0
total_occurences = 0
i = 0
filename = "D:\DEV\mobile\lab2\data.csv"
#file = input("Enter path to CDR file: ")

sms_sum = 0  
out_calls_sum = 0
inc_calls_sum = 0

#number = 915642913
#number = input("Enter IP address: ")
number = "192.168.250.59"
#first 1000#b for free
tariff = 1

# initializing the titles and rows
fields = [] 
rows = [] 
rowlist = []
traflist = []
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader)
    print("fields:", fields)
    
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    #print("Total no. of lines in a CDR file: %d"%(csvreader.line_num)) 
  
    #
    # calculating incoming calls tariffication
    for row in rows[1:17450]:
        #if row[3].find(number) != -1:
        if row[3] == number:
            total_traffic = total_traffic + int(row[12])
            total_occurences = total_occurences + 1
            #print(int(row[12]))
            traflist += {(row[1], row[12])}
        #if row[4].find(number) != -1:
        if row[4] == number:
            total_traffic = total_traffic + int(row[12])
            total_occurences = total_occurences + 1
            #print(int(row[12]))
            traflist += {(row[1], row[12])}
    c = ""
    # total price
    #total_price = sms_price+out_calls_price+inc_calls_price
    if total_traffic < 1000:
        c = "bytes"
        total_cost = (total_traffic*1000-1000)*1/1000000000
        if total_cost < 0:
            total_cost = 0
    if 1000000 > total_traffic > 1000:
        total_traffic = total_traffic/1000
        c = "kilobytes"
        total_cost = (total_traffic*1000-1000)*1/1000000
        if total_cost < 0:
            total_cost = 0
    if 1000000000 > total_traffic > 1000000:
        total_traffic = total_traffic/1000000
        c = "megabytes"
        total_cost = (total_traffic-1)*1
        if total_cost < 0:
            total_cost = 0
    print("total traffic:", total_traffic, c)
    #print("total occurences:", total_occurences)
    print("total cost: ", round(total_cost, 2), "rubles")
    #print(traflist)

with open('out.csv', 'w', newline='') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    for traflist in traflist:
        wr.writerow(traflist)
resultFile.close

############
### plot ###
############

i = 0
globalrow = ""
globaltraf = 0
rows = []
temptraf = 0
newdate = []
newtraf = []
with open('out.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader: 
        rows.append(row) 
    csvfile.close

print(rows)

for row in rows:
    if row[0] == globalrow:
        #print("Plus", row[1])
        temptraf = temptraf + int(row[1])
    else:
        if temptraf != 0:
            newtraf += {temptraf}
        #print("total: ", temptraf)
        #print("new iteration: ", row[0])
        temptraf = int(row[1])
        newdate += {row[0]}
        globalrow = row[0]
        #print(globalrow)
newtraf += {int(row[1])}
#print(len(newdate), newdate)
#print(len(newtraf), newtraf)
 
x = newdate
y = newtraf

plt.plot(x,y, marker='o')

plt.title('Data from the CSV File: Traffic during the time period')

plt.xlabel('time')
plt.ylabel('traffic, bytes')

plt.show()
