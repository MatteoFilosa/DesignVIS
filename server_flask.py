from flask import Flask, render_template, jsonify, make_response, request, send_file
from flask_cors import CORS
from flask_caching import Cache
#from flask_pymongo import PyMongo

import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

CORS(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route("/")
def home():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
