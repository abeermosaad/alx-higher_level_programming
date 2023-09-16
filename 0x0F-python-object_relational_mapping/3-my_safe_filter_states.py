#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import re
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
    x = re.match("[A-Za-z\s]+", argv[4])
    print(x[0])

    query = """SELECT * FROM states
    WHERE BINARY name = '{}' ORDER BY ID ASC""".format(x[0])

    mycursor.execute(query)

    result = mycursor.fetchall()
    for row in result:
        print(row)
    mycursor.close()
    mydb.close()
