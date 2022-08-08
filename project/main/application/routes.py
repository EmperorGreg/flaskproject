from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect, url_for
import sys



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/even',methods=['GET','POST'])
def even():
    formData = request.form.get('number')
    isEven = False
    if formData % 2 != 0:
        return isEven
    else:
        isEven = true
        return isEven
    

return render_template('.html', formData=formData, isEven.)
