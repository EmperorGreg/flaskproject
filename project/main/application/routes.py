from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect, url_for
import sys



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/even',methods=['GET','POST'])
def even(number):
    isEven = False
    if number % 2 != 0:
        return isEven
    else:
        isEven = true
        return isEven

@app.route('/result')
def result():
    formData = request.form.get('number')
    formData = int(formData)
    checkEven = even(formData)
    return render_template('result.html', formData=formData, checkEven=checkEven.text)


