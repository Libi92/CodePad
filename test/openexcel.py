

import pyexcel as pe
import pyexcel.ext.xls
import pyexcel.ext.xlsx

records = pe.get_records(file_name="/Users/cyberprism/Desktop/CSE_S4.xlsx")
for record in records:
    print(record['firstname'], record['lastname'])