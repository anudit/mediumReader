import requests
import bs4
from flask import Flask, render_template, request, redirect, send_file
import jinja2
import os
import markdown2
from MediumParser import parse
import io
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
        return render_template('read.html', ArticleTitle = title, ArticleAuthor = author, ArticleHTML = data, MdLink = '/md/'+url)
    else:
        return "Invalid URL"

@app.route('/md/<path:url>')
def md(url):
    request = requests.get(url)
    if request.status_code == 200:
        try:
            title, author, data  = parse(url)
        except:
            return "Invalid URL"

        proxy = io.StringIO()
        proxy.write(str(data))

        mem = io.BytesIO()
        mem.write(proxy.getvalue().encode('utf-8'))
        mem.seek(0)
        proxy.close()

        return send_file(
            mem,
            as_attachment=True,
            attachment_filename=f'{ title }.md',
            mimetype='text/markdown'
        )

    else:
        return "Invalid URL"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port)
