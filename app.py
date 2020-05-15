from flask import Flask
from flask import render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/grants')
def grant_page():
    return render_template('grants.html')

@app.route('/loans')
def loan_page():
    return render_template('loans.html')

@app.route('/crowdsourcing')
def crowdsourcing():
    return render_template('crowdsourcing.html')

@app.route('/index2')
def home_page2():
    return render_template("index2.html")