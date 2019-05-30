import requests
import numpy as np
import cv2
from matplotlib import pyplot as plt


f = open('africa.jpg', 'wb')
f.write(requests.get('https://upload.wikimedia.org/wikipedia/commons/e/ed/Africa_%28satellite_image%29.jpg').content)
f.close()

obraz_rgb = cv2.imread('africa.jpg')
color = ('b','g','r')
plt.figure(figsize=(15,5), dpi= 80)
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(obraz_rgb,cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2)
for i,col in enumerate(color):
    histr = cv2.calcHist([obraz_rgb],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

