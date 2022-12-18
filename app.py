from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import json
import urllib.request
import os
from datetime import datetime
import pandas as pd
data=pd.read_csv('panace_ingridients.csv')
data2=pd.read_csv('panace_fooditems.csv')
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/panace'
# app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# db = SQLAlchemy(app)
# class Dishes(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     ingridients = db.Column(db.String(12), nullable=False)
#     cuisine= db.Column(db.String(120), nullable=False)
# @app.route("/")
# def home():
#     return render_template('index.html')
@app.route("/south.html")
def home4():  
    return render_template('south.html')
@app.route("/about.html")
def home1():
    return render_template('about.html')
@app.route("/contact.html")
def home2():
    return render_template('contact.html')
# @app.route("/first/<string:post_slug>/", methods=['GET'])
# def sep(post_slug):
#     x=data2.loc[data2['TranslatedRecipeName']==post_slug]
#     a=list(x.Ingridients)
#     b=[]
#     f=''
#     for i in a[0]:
#          if(i!=','):
#               f+=i
#          else:
#               b.append(f)
#               f=''

#     ans=[]
#     for i in b:
#         y=data.loc[data['Ingridient']==i]
#         x=[list(y.Ingridient),list(y.Calories),list(y.Cholesterol),list(y.Sodium),list(y.Fat),list(y.Sugar),list(y.Protein),list(y.vm)]
#         print(x)
#         s=[]
#         for j in x:
#            s.append(j[0])
#         ans.append(s)
#     return render_template('sample.html',param=post_slug,anss=ans)

@app.route("/")
def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("movies.html", movies=dict["results"])