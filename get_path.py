import numpy as np
import cv2 as cv
import json

im = cv.imread('images/cat2.jpg')

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


#cv.drawContours(im, contours, -1, (255,255,0), 3)
#cv.waitKey()
json_file = open("coors.json", "w")  

json_arr = list()

flat_list = []
for sublist in contours:
    for item in sublist:
        flat_list.append(item)


for cont in flat_list:
  coor  = {
    'x': int(cont[0][0]),
    'y': int(cont[0][1])
  }
  json_arr.append(coor)


json_file.writelines(json.dumps(json_arr))
json_file.close() 