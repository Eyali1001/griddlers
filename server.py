from flask import Flask, g, request
import sqlite3

# initializing constants
app = Flask(__name__)
DATABASE = 'database.db'


@app.route('/upload', methods=['POST'])
def upload():
    db = get_db()
    c = db.cursor()
    c.execute('INSERT INTO grids (name,grid) value (?,?)', (request.form['n'], request.form['g']))
    db.commit()
    print ("success")
    return "Done"


@app.route('/download/<name>', methods=['GET'])
def download():
    pass


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# init_db()
app.config["DEBUG"] = True
app.run()
