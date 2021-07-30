import sys
import json
import csv
import sqlite3
con = sqlite3.connect(':memory:')
print('ok')
cursor= con.cursor()
cursor.execute('create table details (id integer, date text, company text, funtype text)')
print('Table created.')
def read_json_file(paath):
    with open(paath) as f:
        data=json.load(f)
        a=(data['response'][0]['data']['schemelist']['scheme'])
    with open('new.csv','w',newline='') as file:
        for i in a:
            b=[(i['osch'],i['StartedOnDate'],i['CompanyLongName'],i['FundHouse'])]
            writer = csv.writer(file)
            writer.writerows(b)
    with open('sample.csv') as f:
        csv_reader= csv.reader(f)
        a=[]
        for i in csv_reader:
            a.append(i)
        print(a)
read_json_file("MF.json")