#%%
from flask import Flask, jsonify
import random
from flask_cors import CORS
from requests import request

keyl = ['OK', 'NG']


def function():
  global keyval
  keyval = random.choice(keyl)



app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def test():
    function()
    key = keyval
    return key

if __name__ == "__main__":
    app.run(debug=True)
