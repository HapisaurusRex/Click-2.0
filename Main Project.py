import numpy as np
from PIL import ImageGrab
from matplotlib import pyplot as plt
import cv2
import time
import pyautogui

def orient_screen():
    calibration_screen = np.array(ImageGrab.grab()) #get the entire screenshot

    cal_top_left = cv2.imread('Top_left_corner.jpg')
    cal_top_right = cv2.imread('Top_right_corner.jpg')
    cal_bot_left = cv2.imread('bottom_left_corner.jpg')

    cal_topL = np.where(cv2.matchTemplate(calibration_screen, cal_top_left, cv2.TM_CCOEFF) > 0.8)
    cal_topR = np.where(cv2.matchTemplate(calibration_screen, cal_top_right, cv2.TM_CCOEFF) > 0.8)
    cal_botL = np.where(cv2.matchTemplate(calibration_screen, cal_bot_left, cv2.TM_CCOEFF) > 0.8)
    '''
    print(cal_topL)
    print(cal_topR)
    print(cal_botL)
    '''
    #use 3 images to orient screen (top left, top right, bottom left)

def screen_record(): 
    last_time = time.time()
    template = cv2.imread('granny.jpg',0) #open the image we are looking for
    w, h = template.shape[::-1]
    while(True):
        printscreen =  np.array(ImageGrab.grab(bbox=(1400,340,1720,800))) #(0,40,1720,1440) whole cookie clicker screen
        processed = cv2.cvtColor(printscreen,cv2.COLOR_BGR2GRAY) #convert to gray scale for processing

        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

        res = cv2.matchTemplate(processed,template,cv2.TM_CCOEFF_NORMED) #perform template match
        threshold = 0.8
        loc = np.where( res >= threshold) #stores top left corner coordiante where a match was found
        for pt in zip(*loc[::-1]): #debug code to see what it found, last time
            cv2.rectangle(printscreen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imwrite('res.png',printscreen)
        time.sleep(5)
        x = loc[0]+1400 #convert to pyauto coordinate
        y = loc[1]+420 #convert to pyauto coordinate
        pyautogui.click(x, y) #click in x,y location

        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows() 
            break

screen_record()

#img_rgb = cv2.imread('Test2.jpg') #open the inventory image 
#img_gray = cv2.imread('Test2.jpg',0) #cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
#template = cv2.imread('granny.jpg',0) #open the image we are looking for


orient_screen()

