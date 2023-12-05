from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import text  #new

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://harry:910615@127.0.0.1:5432/hotel'
db = SQLAlchemy(app)

@app.route('/')
def index():
    sql = """
    CREATE TABLE formuser (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));

    CREATE TABLE hoteluser (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));

    CREATE TABLE booking (
    id serial NOT NULL,
    bid character varying(50) NOT NULL,
    roomtype character varying(20) NOT NULL,
    roomamount character varying(5) NOT NULL,
    datein character varying(20) NOT NULL,
    dateout character varying(20) NOT NULL,
    PRIMARY KEY (id));
    """
    db.session.execute(text(sql))  #new
    db.session.commit()
    return "資料表建立成功！"

if __name__ == '__main__':
   app.run()