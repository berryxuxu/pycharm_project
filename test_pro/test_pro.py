from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from LoginForm import LoginForm
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def login():
	myForm = LoginForm(request.form)
	if request.method=='POST':
		if myForm.username.data=="jikexueyuan" and myForm.password.data=="123456" and myForm.validate():
			return redirect("http://www.jikexueyuan.com")
		else:
			message="Login Failed"
			return render_template('indexx.html',message=message,form=myForm)
	return render_template('indexx.html',form=myForm)

if __name__ == "__main__":
	app.run(port=8081)