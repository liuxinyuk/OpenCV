import numpy as np 
import cv2
import matplotlib.pyplot as plot
import time

#frame is the capture of CAM
#提取圆形的感兴趣区域，其实就是mask操作了

ROI = np.zeros(frame.shape, np.uint8)      #感兴趣区域ROI
cv2.circle(ROI, (cx,cy), d, (255, 255, 255), -1)   #画白圆,圆心(cx,cy),直径，-1是填充
imgroi= ROI & frame            #图像位与
