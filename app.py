from random import gauss
from flask import Flask, render_template, send_file, request
from string import ascii_letters
from utils.cr import Client
from utils.gr import graphing, graphing_random
from utils.sc import searchingW
from utils.rr import read_Readme, auto_Render
from utils.pp import show_img
from time import sleep
from os import remove as rm
app = Flask(__name__)

app.jinja_env.globals.update(gauss=gauss)
@app.route('/')
def index():
    return render_template('index.html', content=read_Readme())

@app.route('/imgb')
def img_bw():
    return render_template('upload.html')

@app.route('/proccimg', methods=['GET','POST'])
def proc_image():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        show_img(f)
        rm(f.filename)
        return send_file('tmp\max.png')

@app.route('/render/<fp>')
def render_code(fp):
    return render_template('code.html', content=auto_Render(fp))

@app.route('/rsa/<passw>')
def rsa(passw):
    return render_template('base.html', client=Client(passw))


@app.route('/graph/<a>/<b>/<c>/<n>')
def enc(a, b, c, n):
    try:
        graphing(int(a), int(b), int(c), int(n))
        return send_file('tmp\graph.png')
    except:
        return render_template('index.html')
@app.route('/graph/r')
def graphing_r():
    try:
        graphing_random()
        return send_file('tmp\graph.png')
    except:
        return render_template('index.html')


@app.route('/wiki/<search>')
def wiki_Search(search):
    x = searchingW(search)
    return render_template('wikie.html',x=x, search=search)


if __name__ == "__main__":
    app.run(debug=True)

