from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

# db connection string
# <protocol>://<user>:<pass>@<host>:<port>/db_name>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://orm_dev:123456@localhost:5432/orm_db'

db = SQLAlchemy(app)


@app.route('/')
def home():
    return 'Hello!'
