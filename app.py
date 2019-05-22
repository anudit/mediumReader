import requests
import bs4
from flask import Flask, render_template, request, redirect
import jinja2
import os
import markdown2
from MediumParser import parse
import time;

def getTS():
    ts = time.time()
    print(str(int(ts)))

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/read/<path:url>')
def convert(url):
    request = requests.get(url)
    if request.status_code == 200:
        try:
            title, author, data  = parse(url)
        except:
            return "Invalid URL"
        data = markdown2.markdown(data)
        return render_template('read.html', ArticleTitle = title, ArticleAuthor = author, ArticleHTML = data)
    else:
        return "Invalid URL"

@app.route('/pdf/<path:url>')
def convert(url):
    request = requests.get(url)
    if request.status_code == 200:
        try:
            title, author, data  = parse(url)
        except:
            return "Invalid URL"
        data = markdown2.markdown(data)
        return render_template('read.html', ArticleTitle = title, ArticleAuthor = author, ArticleHTML = data)
    else:
        return "Invalid URL"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port)
