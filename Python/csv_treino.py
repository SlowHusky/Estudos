#link usado para o csv:https://goo.gl/3zaUlD 

path = "/home/slowhusky/Downloads/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path, mode='r')
lines = [line for line in file]

print(lines[0])
#vai mostrar a estrutura do arquivo (na verdade mostra a primeira linha)
#
#Date,Open,High,Low,Close,Volume,Adj Close
print(lines[0].strip())
#divide separado por ','
print(lines[0].strip().split(','))


dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])
