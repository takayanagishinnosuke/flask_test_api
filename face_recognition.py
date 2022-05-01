import cv2
import numpy as np
import os 
from time import sleep
import app

##-判定関数--##
def recognition(post):
    key = '' 

    ##--カスケードファイルの指定--##
    cascadePath = "haarcascade_frontalface_default.xml"
    ##--カスケードモデルの定義--##
    faceCascade = cv2.CascadeClassifier(cascadePath);

    # img = cv2.imread('test.jpg') #テスト用
    
    img = post

    faces = faceCascade.detectMultiScale( 
        img,
        scaleFactor = 1.2,
        minNeighbors = 5,
    )
    ##--facesがあるかないか判定する--##
    if (len(faces) > 0):
        key = 'Danger'
    else:
        key = "NoProblem"
    
    return key

