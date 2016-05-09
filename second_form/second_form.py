#coding=utf-8
from flask import Flask, render_template, request, redirect
from Myform import Myform
from db import Email_Table
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():
    myform = Myform(request.form) # 视图函数中创建表单
    if request.method == 'POST':
        if myform.email.data and myform.validate() : #视图函数中获取表单值
            user_email = Email_Table(myform.email.data)
            message = 'Success ' + user_email.select_email()[0][0]
            return render_template('indexxx.html',message=message, form=myform)
        else:
            message = 'Email failed'
            return render_template('indexxx.html', message=message, form=myform)
    return render_template('indexxx.html', form=myform)

@app.route('/success')
def login_success():
    return render_template('successs.html')

if __name__ == '__main__':
    app.run()
