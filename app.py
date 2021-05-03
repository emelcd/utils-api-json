from random import gauss
from flask import Flask, render_template, send_file
from string import ascii_letters
from utils.cr import Client
from utils.gr import graphing, graphing_random
from utils.sc import searchingW
from utils.rr import read_Readme, auto_Render
app = Flask(__name__)

app.jinja_env.globals.update(gauss=gauss)

@app.route('/')
def index():
    return render_template('index.html', content=read_Readme())

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
