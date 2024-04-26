import requests
# import re
import time
import json
# from bs4 import BeautifulSoup
import os
import sys
# from requests.api import patch


class CoserCreeper:
    def __init__(self,url = r"https://zfile.cosersets.com/api/list/1?path=%2F"):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.url = url

    def get_one_page(self,url):
        """
        :param url: 目标地址
        :return: 返回html
        """
        def getPage(url):
            time.sleep(0.1)
            response = requests.get(url,headers = self.headers)
            if response.status_code == 200:
                return response
            else:
                print("going to reconnect")
                return None
        i = 0
        r = None
        while not r and i<20:
            r = getPage(url)
            i += 1
        return r
        # return response
    

    def calUrl(self,url,path = [], password = "", orderBy = "", orderDirection = ""):
        if path:
            tempPath = "/".join(path)
        else:
            tempPath = ""
        totalUrl = url + tempPath + "&password=" + password + "&orderBy=" + orderBy + "&orderDirection=" + orderDirection
        return totalUrl

    def saveContent(self,url,path):
        """写入内容"""
        response = self.get_one_page(url)
        if not response:
            print(path)
            print("download error")
            return
        notNamePath = "\\".join(path[:-1])
        totalPath = "\\".join(path)
        if os.path.exists(notNamePath):
            pass
        else:
            os.makedirs(notNamePath)
        with open(totalPath,"wb+") as fw:
            fw.write(response.content)
        print("saving "+"\\".join(path))

    def dumpOnePage(self,path = [], password = "", orderBy = "", orderDirection = ""):
        """
        解析一个页面
        """
        totalUrl = self.calUrl(self.url,path,password,orderBy,orderDirection)
        response = self.get_one_page(totalUrl)
        if response:
            fileInJson = response.text
        else:
            return []
        file_dic = json.loads(fileInJson)
        return file_dic["data"]["files"]

    def downloadOneContent(self,path,base):
        """下载一个内容"""
        baseUrl = r"https://zfile.cosersets.com/file/1/"
        url = baseUrl + "/".join(path)
        savepath = [base] + path
        if os.path.exists("\\".join(savepath)):
            print("has downloaded " +"\\".join(savepath))
            return # 已经有了
        self.saveContent(url,savepath)

    def downloadOneDir(self,path = [],base = "D:\\Coser",index = [0]):
        print("start download" + "/".join(path))
        files = self.dumpOnePage(path) # 这一步获得file列表
        if not files:
            return # 此时找到了最子节点
        for f in files:
            # print(f)
            newPath = path[:]
            newPath.append(f["name"])
            if f["type"] == "FOLDER":
                # 说明是文件夹，继续向下搜索    
                self.downloadOneDir(path = newPath, base = base)
            else:
                # 说明有内容，保存下来
                self.downloadOneContent(path = newPath,base=base)
            index[0] += 1
exitFlag = False

# from func_timeout import func_set_timeout, FunctionTimedOut

def downloadCoserSets(name):
    global exitFlag
    CC = CoserCreeper()
    # files = CC.dumpMainPage()
    # firstCoser = CC.dumpCoserPage(0,files)
    # print(files)
    # path = ["Azami","2B Shinobi","001.webp"]
    # CC.downloadOneSet(path)
    # path = ["樱群"]
    files = CC.dumpOnePage()
    if isinstance(name,str):
        for k in range(len(files)):
            if files[k]['name'] == name:
                break
        newfiles = files[k:]
    else:
        newfiles = files[name:]
    for nf in newfiles:
        path = [nf['name']]
        CC.downloadOneDir(path,base="F:\\aisyoujyo\\CoserSets")# 获取当前download了多少个文件
    # 001.webp
    exitFlag = True

import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, func, i = None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.func = func
        self.i = i
    def run(self):
        print ("开始线程：" + self.name)
        # print_time(self.name, self.counter, 5)
        if self.i:
            self.func(self.i)
        else:
            self.func()
        print ("退出线程：" + self.name)
    

index = [0]
start = 0
def Timer(Timer = "CoserDownloader Timer"):
    # 万一主进程卡了，用这个来唤醒
    # global index
    # global start
    # watchDog = 0
    # lastIndex = [0]
    while not exitFlag:
        # print(exitFlag)
        time.sleep(1)
        print ("%s: %s" % (Timer, time.ctime(time.time())))
        # if lastIndex[0] == index[0]:
        #     watchDog += 1
        # else:
        #     lastIndex = index
        #     watchDog = 0 # 看门狗复位
        # if watchDog > 100:
        #     thread1.stop
        #     # 重启进程
        #     thread1Re = myThread(2,"Thread-2",downloadCoserSets,lastIndex[0] + start)
        #     thread1Re.join()
            


def main():
    path = "F:\\aisyoujyo\\CoserSets"
    files= os.listdir(path) #得到文件夹下的所有文件名称
    print(files)
    # arg = sys.argv[1]
    arg = len(files) - 1
    downloadCoserSets(arg)
    # print("起始位置: ",arg)
    # # 创建新线程
    # thread1 = myThread(1, "Thread-1", Timer)
    # thread2 = myThread(2, "Thread-2", downloadCoserSets, arg)

    # # 开启新线程
    # thread1.start()
    # thread2.start()

    # thread1.join()
    # thread2.join()
    # print ("退出主线程")
import schedule
if __name__ == "__main__":
    main()
    # schedule.every().hours(4).do(main) 
    # while True:
    #     schedule.run_pending()