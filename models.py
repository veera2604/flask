from flask import Flask,render_template,request,redirect

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///user.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False



db=SQLAlchemy(app)


class Data(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    email=db.Column(db.String(30))
    
    