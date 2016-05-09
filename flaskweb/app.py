#coding:utf-8
from flask import Flask, render_template, request, flash, redirect
from flask.ext.bootstrap import Bootstrap
from MyForm import Myform
from db import Email_Table
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = '1010'

@app.route('/12')
def mainpage():
    return render_template('mainpage.html')
@app.route('/1')
def one():
    return render_template('child1.html')
@app.route('/2')
def two():
    return render_template('child2.html')

@app.route('/', methods=['GET','POST'])
def submit():
    myform = Myform(request.form)
    if request.method == 'POST':
        if myform.email.data and myform.validate():  # 视图函数中获取表单值
            user_email = Email_Table(myform.email.data, myform.text_aera.data)
            #user_name = user_email.select_email()
            myform = None
            return render_template('success.html')
        else:
            flash('Can not be empty')
            return redirect('/')
    return render_template('mainpage.html',form=myform)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internak_server_error(error):
    return render_template('500.html'), 500
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()
