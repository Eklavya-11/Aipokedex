from flask import request
import urllib.parse
from __main__ import app
from helpers.ai import solve

@app.route('/identify', methods = ["POST"])
def result():
    url = urllib.parse.unquote(request.form['imgurl'])

    pokemon = solve(url)

    return pokemon
