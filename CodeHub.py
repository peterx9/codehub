from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Configure SQLite database
DATABASE = 'database.db'

def create_table():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, title TEXT, url TEXT)''')
    connection.commit()
    connection.close()

@app.route('/')
def index():
    create_table()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
