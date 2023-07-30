####################################################################################################
#*Importing Modules

import openpyxl as xl
import mysql.connector as msc
from datetime import time

####################################################################################################
#* Connecting to Database and creating a cursor

connec = msc.connect(user = 'root', password='6124', host='localhost', database='metro')
print("Connected to mysql Database Successfully."if connec.is_connected() else "Connection Failed.")
cur = connec.cursor()

####################################################################################################

 #! Khapri to Kasturchand Park
 #* (1) Khapri - Khapri (12)
 #* (2) New Airport - New (11)
 #* (3) Airport South - South (10)
 #* (4) Airport - Airport (9)
 #* (5) Ujjwal Nagar - Ujjwal (8)
 #* (6) Jaiprakash Nagar - Jaiprakash (7)
 #* (7) Ajni Sq. - Ajni (6)
 #* (8) Rahate colony - Rahate (5)
 #* (9) Congress Nagar - congress (4)
 #* (10) Sitabuldi - Sitabuldi (3)
 #* (11) Zero Mile - Zero (2)
 #* (12) Kasturchand Park - Kasturchand (1)

 #! Sitabuldi to Lokmanya Nagar
 #* (1) Sitabuldi - Sitabuldi (11)
 #* (2) Jhansi Rani Sq. - Jhanshi (10)
 #* (3) Institute of Engineering - IOE (9)
 #* (4) Shankar Nagar - Shankar (8)
 #* (5) LAD Sq. - LAD (7)
 #* (6) Dharampeth College - Dharampeth (6)
 #* (7) Subhash Nagar - Subhash (5)
 #* (8) Rachna Ring Road - Rachna (4)
 #* (9) Vasudev Nagar - Vasudev (3)
 #* (10) Bansi Nagar - bansi (2)
 #* (11) Lokmanya Nagar - Lokmanya (1)

####################################################################################################
#! Creating Tables

# Line_1_Up
Q1 = """Create Table Line_1_Up(Series int(5), Kasturchand varchar(8), Zero varchar(8), Sitabuldi varchar(8),
Congress varchar(8), Rahate varchar(8), Ajni varchar(8), Chhatrapati varchar(8), Jaiprakash varchar(8),
Ujjwal varchar(8), Airport varchar(8), South varchar(8), New varchar(8), Khapri varchar(8))"""

try:
    cur.execute(Q1)
    print("Table 1 Created.")
except:
    print("Table 1 either not created or it already exsists")

# Line_1_Down
Q2 = '''Create Table Line_1_Down(Series int(5), Khapri varchar(8), New varchar(8), South varchar(8),
Airport varchar(8), Ujjwal varchar(8), Jaiprakash varchar(8), Chhatrapati varchar(8), Ajni varchar(8),
Rahate varchar(8), Congress varchar(8), Sitabuldi varchar(8), Zero varchar(8), Kasturchand varchar(8))'''

try:
    cur.execute(Q2)
    print("Table 2 Created.")
except:
    print("Table 2 either not created or it already exsists")

# Line_2_Up
Q3 = '''Create Table Line_2_Up(Series int(5), Sitabuldi varchar(8), Jhansi varchar(8), IOE varchar(8),
Shankar varchar(8), LAD varchar(8), Dharampeth varchar(8), Subhash varchar(8), Rachna varchar(8),
Vasudev varchar(8), Bansi varchar(8), Lokmanya varchar(8))'''

try:
    cur.execute(Q3)
    print("Table 3 Created.")
except:
    print("Table 3 either not created or it already exsists")

# Line_2_Down
Q4 = '''Create Table Line_2_Down(Series int(5), Lokmanya varchar(8), Bansi varchar(8), Vasudev varchar(8),
Rachna varchar(8), Subhash varchar(8), Dharampeth varchar(8), LAD varchar(8), Shankar varchar(8),
IOE varchar(8), Jhansi varchar(8), Sitabuldi varchar(8))'''

try:
    cur.execute(Q4)
    print("Table 4 Created.")
except:
    print("Table 4 either not created or it already exsists")

####################################################################################################

tm = "6:10:45"
t = list(map(int, tm.split(':')))
print(time(t[0],t[1],t[2]))

####################################################################################################
#* Adding Excelsheets to the program and activating

path1 = "D:\Coding\Metro mini project\Line 1 Khapri - Kasturchand.xlsx"
path2 = "D:\Coding\Metro mini project\Line 2 Lokmanya - Sitabuldi.xlsx"

wb_l1 = xl.load_workbook(path1)
wb_l2 = xl.load_workbook(path2)

sheet1 = wb_l1.active
sheet2 = wb_l2.active

Table1_up = sheet1['C2':'BM15']
Table1_down = sheet1['C21':'BM34']

Table2_up = sheet2['C19':'BM30']
Table2_down = sheet2['C2':'BM13']

####################################################################################################

line = 1
timings = []
database_l1u = []
for i in Table1_up:
    for j in i:
        timings.append(j.value)
        if line == 63: database_l1u.append(timings); timings.clear(); line= 1; continue
        line += 1


####################################################################################################

def add(table):
    line, timings, database = 1, [], []
    for i in table:
        for j in i:
            timings.append(j.value)
            if line == 63: database.append(timings); timings.clear(); line= 1; continue
            line += 1

    trip = []
    for x in range(63):
        for y in range(len(database)):
            trip.append(database[y][x])
            
# add(0,0,Table1_up,0,0)

####################################################################################################