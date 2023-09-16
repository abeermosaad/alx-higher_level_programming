#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    mydb = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    mycursor = mydb.cursor()
    string = argv[4].split('\';')
    print(string[0])

    query = """SELECT * FROM states
    WHERE BINARY name = '{}' ORDER BY ID ASC""".format(string[0])

    mycursor.execute(query)

    result = mycursor.fetchall()
    for row in result:
        print(row)
    mycursor.close()
    mydb.close()
