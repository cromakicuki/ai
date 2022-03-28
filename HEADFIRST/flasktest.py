from flask import Flask
from webapp.vsearch import search4letters
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask 홍길동'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universse and everything'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title = 'Welcome to search4')
app.run()