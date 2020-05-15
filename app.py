from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Database
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User(db.Model):
    user_name = db.Column(db.String(255), primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    first_name = db.Column(db.String(255), unique=False)
    last_name = db.Column(db.String(255), unique=False)

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


if __name__ == '__main__':
    app.run()