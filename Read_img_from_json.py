import base64
import json
import numpy as np
import cv2

filepath='C:/Users/king/OneDrive/program/rw_json/test.json'

def read_img_from_json(path):
    # 读取 json 文件，并直接存入字典
    with open(path, "r") as json_file:
        raw_data = json.load(json_file) 
    # 从字典中取得图片的 base64 字符串，形如“YABgAAD/2wBDAAYEBQYFBAY...."，
    image_base64_string = raw_data["imageData"]    
    # 将 base64 字符串解码成图片字节码
    image_data = base64.b64decode(image_base64_string)    
    #string to np
    nparr = np.fromstring(image_data,np.uint8)  
    img_np = cv2.imdecode(nparr,1) 
    
    info = raw_data["shapes"]
    return img_np,info
    
image ,info= read_img_from_json(filepath)
