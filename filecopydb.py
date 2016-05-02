import sqlite3
import datetime
import time

conn = sqlite3.connect('copyrecord.db')

def createTable():
    conn.execute('CREATE TABLE if not exists TRANSFER_DATESTAMP (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        TEXTDATE TEXT,\
        INTDATE INT);')

def getLastUpdate():
    sql_str = "SELECT * FROM TRANSFER_DATESTAMP WHERE ID = (SELECT max(ID) FROM TRANSFER_DATESTAMP)"
    cursor = conn.execute(sql_str)

    # Get data from cursor in array
    lastupdate = cursor.fetchone()
    return lastupdate

def addLatestUpdate():
    textdate = str(datetime.datetime.now())
    intdate = str(time.time())
    # Create values part of sql command
    val_str = "'" + textdate + "', '" +intdate + "'"
    # Create sql query
    sql_str = "INSERT INTO TRANSFER_DATESTAMP (TEXTDATE, INTDATE) VALUES (" + val_str + ");"

    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def main():
    createTable()
    getLastUpdate()

if __name__ == '__main__':
    main()
