from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

# db connection string
# <protocol>://<user>:<pass>@<host>:<port>/db_name>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://orm_dev:123456@localhost:5432/orm_db'

db = SQLAlchemy(app)

# Model
# Just declares and configures the model in memory - the physical DB is unaffected
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float(precision=2))
    stock = db.Column(db.Integer, db.CheckConstraint('stock>=0'))




@app.route('/')
def home():
    return 'Hello!'
