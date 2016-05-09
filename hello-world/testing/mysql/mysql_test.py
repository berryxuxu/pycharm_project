# coding=utf-8
import MySQLdb

db = MySQLdb.connect('localhost','root','159632','first')

cursor = db.cursor()

cursor.execute('''  ''')

data = cursor.fetchall()
print data

db.commit()
db.close()