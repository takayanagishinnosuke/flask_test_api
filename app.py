from crypt import methods
from distutils.log import error
from flask import Flask, jsonify, request, url_for
import json
import base64
from io import BytesIO
from flask_cors import CORS
import numpy as np
import cv2
import face_recognition

img_gray =[] #np配列入れるリストを用意

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app)

@app.route('/', methods=("GET", 'POST'))
def test():
  if request.method == 'POST':
    posted = request.get_json()
    key = posted['img'] ##imgというjsonのbodyで入ってきたら
    
    img_stream = base64.b64decode(key) ##keyをデコード
    img_array = np.asarray(bytearray(img_stream), dtype=np.uint8) #np配列に
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR) #opencvで使える形式に
    
    global img_gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ##白黒に
    
    #cv2.imwrite('test.jpg',img_gray) ##テストでjpg保存
    ## recognition関数へ渡す
    key = face_recognition.recognition(img_gray)
    print(key) ##確認用

    return jsonify({"result": key}) ##jsonにして返す


  else:
    return jsonify({"result": "POST失敗 エラー"})


if __name__ == "__main__":
    app.run(port=5000)
