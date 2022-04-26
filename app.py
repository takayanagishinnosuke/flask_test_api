from flask import Flask, jsonify
import random
from flask_cors import CORS
from requests import request

keyval = 0


def function():
  global keyval
  keyval = random.randint(0,1)


app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def test():
    function()
    return jsonify({'key': keyval})

if __name__ == "__main__":
    app.run(debug=True)
