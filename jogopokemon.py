from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/pokemon')
def inicio():
    return render_template('jogar.html')



@app.route('/pokemon/jogar')
def jogar():
    return render_template('site_pokemon.html')