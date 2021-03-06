#link usado para o csv:https://goo.gl/3zaUlD 
import csv
from datetime import datetime
path = "/home/slowhusky/Downloads/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) #pega a primeira linha que eh o header

data = []
for row in reader:
    date = datetime.strptime(row[0],'%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume= int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low,
                 close, volume, adj_close])

#print(data)

#computar e armazenar o valor diario das acoes
return_path = path = "/home/slowhusky/Documents/Estudos/Python"
file = open(return_path, 'w')
writer = csv.writer(file)
writer.writerow(["Dater","Return"])

for i in range(len(data)-1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
