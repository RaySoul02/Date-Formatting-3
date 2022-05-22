import csv
from datetime import datetime

r = csv.reader(open("source.csv","r"), delimiter =";")
header = next(r)
header1 = ['year', 'region', 'value']
with open('result.csv', 'w') as result:
    writer = csv.writer(result, lineterminator='\n')
    writer.writerow(header1)
    for row in r:
        print(row[0])
        row[0] = datetime.strptime(row[0],'%Y-%b').strftime("%Y-%m-%d")
        if row[0] != "":
            writer.writerow(row)