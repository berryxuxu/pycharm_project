# coding=utf-8
from flask import Flask
from flaskweb import db
from models import UserEmail

def save():
    email = UserEmail('1234')
    db.session.add(email)
    db.session.commit()

def query_all():
    emails = UserEmail.query.all()
    for e in emails:
        print e

