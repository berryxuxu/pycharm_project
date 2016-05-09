from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import MySQLdb
from flaskweb import db
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xcmzozuhnrgksa:_QM5S_gn8RvDwngu64ePXTkAoC@ec2-54-83-12-22.compute-1.amazonaws.com:5432/dbkhdc0qmvagdg'
#db = SQLAlchemy(app)
'''
def get_con():
    host = '127.0.0.1'
    port = 3306
    db = 'first_flask'
    user = 'root'
    password = '159632'
    con = MySQLdb.connect(host=host, user=user, password=password, db=db, port=port, charset='utf-8')
    return con
'''
class UserEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return 'User email: %s'  %self.email
    '''
    def save(self):
        con = get_con()
        cursor = con.cursor()
        sql = 'insert into email(email) value( %s);'
        cursor.execute(sql, (self.email))
        con.commit()
        cursor.close()
        con.close()

    query_all(self):
        con = get_con()
        cursor = con.cursor()
        sql = 'select * from email;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        emails = []
        for r in rows:
            user = UserEmail(r[1])
            emails.append(user)
        con.commit()
        cursor.close()
        con.close()
        return emails
    '''
    def __str__(self):
        return 'email: %s' %self.email