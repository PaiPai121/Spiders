# import os
# import time
# # import cv2
import numpy as np
from PIL import Image,ImageFilter
# from numpy.lib.function_base import diff
# # print()
# path = os.getcwd() + "\\picCache" #文件夹目录

# files= os.listdir(path) #得到文件夹下的所有文件名称
# s = []


# def checkImg(img):
#     img = img.convert("L")
#     return img
    
# def sendMail(content,img):
#     pass

# if __name__=="__main__":
#     threshold = 100000
#     detected = False
#     lastImg = np.ndarray([720,1280])
#     time.sleep(10)
#     for file in files: #遍历文件夹
#         if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
#             print(file)
#             print(time.ctime(os.path.getmtime(path + "\\"+file)))
#             i = Image.open(path + "\\"+file)
#             # 此处获取了图像
#             i = i.convert("L").filter(ImageFilter.GaussianBlur(radius=2)) # 高斯模糊
#             i = np.array(i).astype(np.int)
#             # i= i
#             if not lastImg.any():
#                 lastImg = i # 没有过去存下的图像
#                 continue
#             else:
#                 ## 计算差异
#                 diffImg = np.abs(lastImg - i)
#                 # print(diffImg)
#                 # Image.fromarray(diffImg).show()
                
#                 # 此时的总距离
#                 totaldis = sum(sum(diffImg))
#                 if totaldis > threshold:
#                     # 有运动物体进入
#                     lastImg = i
#                     sendMail(time.ctime(time.time()),i)
#                     print("some detected")
#                     detected = True
#                 else:
#                     lastImg = (i + lastImg) /2 # 缓变的背景
#             os.remove(path + "\\"+file) # 删除这张图
#     if detected:
#         time.sleep(600)# 休息一下
I = Image.fromarray(np.array([[1,2,3]]))
I.show()
I = I.convert("RGB")
I.save("123.jpg")

def savePic(img,path):
    img.convert("RGB")
    img.save(path)