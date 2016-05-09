#coding:utf-8
import os
import psycopg2
import urlparse


urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ['DATABASE_URL'])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

#conn = psycopg2.connect(database="first", user="postgres", password="159632", host="127.0.0.1", port="5432")
cur = conn.cursor()
#print cur
class Email_Table(object):
	def __init__(self, email, message):
		self.email = email
		self.message = message
		try:
			cur.execute('create table if not exists test(id serial primary key, email varchar not null , message varchar)')
			insert_sql = "insert into test (email,message) values ('%s','%s'); "  %(self.email, self.message)
			#cur.execute('select * from users')
			cur.execute(insert_sql)
			conn.commit()
		except:
			conn.commit()
		finally:
			conn.commit()


	def select_all(self):
		select_all_sql = 'SELECT * FROM test'
		cur.execute(select_all_sql)
		conn.commit()
		result = cur.fetchall()
		conn.close()
		return result

	def select_email(self):
		select_email_sql = "SELECT email FROM test WHERE email = '%s' " %(self.email)
		cur.execute(select_email_sql)
		conn.commit()
		result = cur.fetchall()
		conn.close()
		return result[0][0]


# my = Email_Table('3123','333')
# my1 = Email_Table('fadsf','fasd')
# print type(my1.select_email())
