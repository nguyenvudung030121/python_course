import csv

header = ['fruit', 'price']
data = [["xoai",10],["oi",20],["kiwi",15]]

with open('fruit.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
