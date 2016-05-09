from wtforms import Form,TextField,PasswordField,validators,TextAreaField

class Myform(Form): #inheretent from flask-wtf
    email = TextField("email", [validators.Required()])
    text_aera = TextAreaField('text_area',[validators.Required()],default='Please comment here',)