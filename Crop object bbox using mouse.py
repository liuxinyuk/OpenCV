import cv2
import os
import numpy as np
global img,cut_img
global point1, point2
global cp_list
global min_x,min_y,width,height
cp_list=[]
count=1
def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    global min_x,min_y,width,height
    temp = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        point1 = (x,y)
        cv2.circle(temp, point1, 10, (0,255,0), 3)
        cv2.imshow('image', temp)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):      #按住左键拖曳
        cv2.rectangle(temp, point1, (x,y), (255,0,0), 3)
        cv2.imshow('image', temp)
        cv2.waitKey(100)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        point2 = (x,y)
        cv2.rectangle(img, point1, point2, (0,0,255), 3) 
        cv2.imshow('image', img)
        min_x = min(point1[0],point2[0])     
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        #计算框的中心
        midx = (point1[0]+point2[0])/2
        midy = (point1[1]+point2[1])/2
        cp=(midx,midy)
        cp_list.append(cp)
        print(cp_list)
        print(width)
        #cut_img = img[min_y:min_y+height, min_x:min_x+width]
        #cv2.imwrite('lena3.jpg', cut_img)




if __name__ == '__main__':
    '''
    create a new dir:CropImages,saving the cropped img.
    'q'  quit the program
    's'  save the cropped img
    'd'  next img to crop
    '''
    path='D:\\xx\\xx'
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    #目录下如果没有相应的文件夹则新建
    if os.path.exists(path+'//CropImages') == False:
        os.mkdir(path+'//CropImages')
    isquit = 0
    cnt = 1
    prename = "000000"
    
    for imgfile in filelist:
        imgdir=os.path.join(path,imgfile)
        if os.path.isdir(imgdir):continue   #如果是文件夹则跳过
        global img,cut_img
        img = cv2.imread(imgdir)
        rawimg = img.copy() 
        cv2.namedWindow('image',0)
        while(img.shape[0]>0):
            
            cv2.setMouseCallback('image', on_mouse)
            cv2.imshow('image', img)
            
            getkb = cv2.waitKey(200) & 0xFF
            if getkb == ord('d'): break
            elif getkb == ord('q'): 
                isquit = 1
                break
            elif getkb == ord('s'):
                cut_img = rawimg[min_y:min_y+height, min_x:min_x+width]
                cv2.imwrite(path+"\\CropImages\\"+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg",cut_img)
                print ("save to "+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg")
                cnt += 1
        if isquit: break
    
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
