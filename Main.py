####################################################################################################
#*Importing Modules

import openpyxl as xl
import mysql.connector
import datetime

####################################################################################################
#* Connecting to Database and creating a cursor

connec = mysql.connector.connect(user = 'root', password='6124', host='localhost', database='metro')
print("Connected to mysql Database Successfully."if connec.is_connected() else "Connection Failed.")
cur = connec.cursor()

####################################################################################################


Q = "Create Table Line_1_Up(Sr no. INT(5), )"

t = "00:12:34"
t = tuple(int(x) for x in t.split())

print(datetime.time(t[0],t[1],t[2]))

####################################################################################################
#* Addind Excelsheets to the program and activating

path1 = "D:\Coding\Metro mini project\Line 1 Khapri - Kasturchand.xlsx"
path2 = "D:\Coding\Metro mini project\Line 2 Lokmanya - Sitabuldi.xlsx"
wb_l1 = xl.load_workbook(path1)
wb_l2 = xl.load_workbook(path2)
sheet1 = wb_l1.active
sheet2 = wb_l2.active

####################################################################################################

table = sheet1['B2':'BM16']


# for c1 in table:
#     for i in c1:
#         # print(i.value)
connec.close()