# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
import jinja2

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()