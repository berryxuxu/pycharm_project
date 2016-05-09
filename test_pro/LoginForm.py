from wtforms import Form,TextField,PasswordField,validators

class LoginForm(Form):

	username = TextField("username",[validators.Required()])
	password = PasswordField("password",[validators.Required()])