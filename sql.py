import sqlite3


#Connect to sqlite
connection=sqlite3.connect("student.db")

#Cursor creation
cursor = connection.cursor()

#create table
table_info ="""
Create table STUDENT(ID INT,NAME VARCHAR(25),YEAR VARCHAR(25),
GROUPS VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)
## Insert some records
cursor.execute('''Insert Into STUDENT values(1,'Nishanth','4','DataAnalytics',90)''')
cursor.execute('''Insert Into STUDENT values(2,'Bhuvanesh','4','CyberSecurity',94)''')
cursor.execute('''Insert Into STUDENT values(3,'Karthik Raj','4','FullStack',94)''')
cursor.execute('''Insert Into STUDENT values(4,'JP','4','SDE',95)''')
cursor.execute('''Insert Into STUDENT values(5,'Kishore','4','FullStack',93)''')
cursor.execute('''Insert Into STUDENT values(6,'Hareeswar','4','CyberSecurity',91)''')


print("Records are: ")
data = cursor.execute('''Select * FROM STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()