from flask import Flask, render_template
from string import ascii_letters
from utils.cr import Client
app = Flask(__name__)


@app.route('/rsa/<passw>')
def index(passw):
    return render_template('base.html', client=Client(passw) )


app.run(debug=True)
