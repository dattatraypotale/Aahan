import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()


conn = sqlite3.connect('mymobileshoppy.db')
c = conn.cursor()
c.execute("select * from available")
mysel = c.execute("select * from available")

colomn_name = ["ID", "product name", "model number", "IMEI", "HSR", "buy Price", "vendor", "purchec date"]
for j, value in enumerate(colomn_name):
    worksheet.write(0, j, value)

for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i+1, j, value)
workbook.close()