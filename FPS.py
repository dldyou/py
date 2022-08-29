# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:35:04 2020

@author: Deep.i inc.
"""

import cv2
import timeit

# 영상 정보 불러오기
video = cv2.VideoCapture('KITTI.mp4')
# 가우시안 혼합 배경제거 알고리즘
fgbg = cv2.createBackgroundSubtractorMOG2()

def MOG(frame):
    
    fgmask = fgbg.apply(frame)
    _,fgmask = cv2.threshold(fgmask, 175, 255, cv2.THRESH_BINARY)
    results = cv2.findContours(
    fgmask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in results[0]:
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

while True:

    ret, frame = video.read()
    
    if ret is True:
        
        
        # 알고리즘 시작 시점
        start_t = timeit.default_timer()
        
        """ 알고리즘 연산 """
        MOG(frame)
        """ 알고리즘 연산 """
        
        # 알고리즘 종료 시점
        terminate_t = timeit.default_timer()
        cv2.imshow('video',frame)
        FPS = int(1./(terminate_t - start_t ))
        print(FPS)        
        
        if cv2.waitKey(1) > 0 :  
            break
        
        