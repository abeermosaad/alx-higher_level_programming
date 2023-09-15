#!/usr/bin/python3

"""MySQLdb Module"""
import MySQLdb

mydb = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
	db = 'hbtn_0e_0_usa'
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM states ORDER BY ID ASC")

result = mycursor.fetchall()
for row in result:
	print (row)
