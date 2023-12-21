from flask import Flask, render_template
from flask_sqlacademy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
  
def create_db():
    db.create_all()

if __name__ == '__main__':
    create_db()
    app.run(port=5001, debug=True)
