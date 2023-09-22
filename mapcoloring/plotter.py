import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('map.png', cv2.IMREAD_COLOR)
color = []
coor = [(93, 168), (234, 102), (244, 225), 
        (373, 130), (410, 224), (355, 291),(362, 375)]
rgb = {"Red": (255,0,0), "Green": (0,255,0), "Blue": (0,0,255)}

def plot(solution):
    for i in range(len(solution.state_list)):
        color.append(solution.state_list[i].color.color)
        cv2.circle(img, coor[i], 31, rgb[color[i]], -1)
    plt.imshow(img)
    plt.show()