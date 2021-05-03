from random import gauss
from flask import Flask, render_template, send_file
from string import ascii_letters
from utils.cr import Client
from utils.gr import graphing, graphing_random
app = Flask(__name__)

app.jinja_env.globals.update(gauss=gauss)


@app.route('/rsa/<passw>')
def index(passw):
    return render_template('base.html', client=Client(passw))


@app.route('/graph/<a>/<b>/<c>/<n>/<l>')
def enc(a, b, c, n, l):
    try:
        graphing(int(a), int(b), int(c), int(n), int(l))
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


app.run(debug=True)
