# all the imports
from myProject import app
import sqlite3
from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

@app.route('/')
def index():
	return 'Hello World'

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
	app.run(debug=True)