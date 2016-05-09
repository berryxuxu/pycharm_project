import MySQLdb

con = MySQLdb.connect('localhost', 'root','159632','test_flask')
cur = con.cursor()

class Email_Table(object):
	def __init__(self, email):
		self.email = email
		insert_sql = "INSERT INTO email_table(email) VALUE ('%s') "  % (self.email)
		cur.execute(insert_sql)
		con.commit()

	def select_all(self):
		select_all_sql = 'SELECT * FROM email_table'
		cur.execute(select_all_sql)
		con.commit()
		result = cur.fetchall()
		con.close()
		return result

	def select_email(self):
		select_email_sql = "SELECT * FROM email_table WHERE email = '%s' " %(self.email)
		cur.execute(select_email_sql)
		con.commit()
		result = cur.fetchall()
		con.close()
		return result

#my = Email_Table('fh')
#print my.select_email()
