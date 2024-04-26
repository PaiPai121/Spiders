
from turtle import ht
from urllib import response
import requests
import re
import time

from bs4 import BeautifulSoup

from pyquery import PyQuery as pq
from pyquery import PyQuery
class MangaCreeper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }

    def get_one_page(self,url,headers):

        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response
        else:
            self.get_one_page(url,headers)


    def downloadpic(self,url,num,filepath):
        try:
            response = self.get_one_page(url,self.headers)
            if response == None:
                print("download page"+str(num)+'Failed \n')
            else:
                print("successfully download page"+str(num)+'\n')
            with open(filepath +'第' + str(num) +'张.jpg','wb') as fw:
                fw.write(response.content)
            return True
        except:
            return False



    def mkdir(self,path):
        import os
        path = path.strip()#去掉空格
        path = path.rstrip('\\')#去掉尾部反斜杠

        isExists = os.path.exists(path)#路径是否存在
        if not isExists :
            os.makedirs(path)
            return True
        else:
            return False


    def downwords(self,url,num,Begin,End,name):
        basicpath = r'D:\manga\Download' + '\\' + name + '第' + str(Begin) + "-" + str(End)+"话"
        totalpath = basicpath+str('\\第' + str(num) + '话')
        self.mkdir(totalpath)

        flag = True
        for i in range(20):
            if i ==0:
                totalurl = url
            else:
                totalurl = url+ '/index_' +str(i)+'.html'
            if(not self.downloadpic(totalurl,i, totalpath + '\\')):
                break
        print(str(num)+"finished")

    def getName(self, basicUrl):
        """
        获取漫画名称
        """
        html = self.get_one_page(basicUrl,self.headers).text
        soup = BeautifulSoup(html, "lxml")
        meta_list = soup.find_all('meta')
        for meta in meta_list:
            if 'property' in meta.attrs.keys() and meta.attrs['property'] == 'og:title':
                name = meta.attrs['content'].strip()
                break
        return name

    def getList(self,url = "http://www.manmanju.com/comiclist/4/index.htm"):
        html = self.get_one_page(url,self.headers).text
        # doc = pq(html,encoding="utf-8")
        doc = PyQuery(url,encoding = "GBK")
        i = 0
        res = []
        resurl = []
        for item in doc('dd')('a').items():
            if i >= 3:
                i = 0
            i += 1
            if i == 2 or i == 3:
                continue
            resurl.append(item.attr("href"))
            res.append(item.text())
        return resurl,res

    def downonehua(self,url,num,Begin,End,name):
        basicpath = r'D:\manga\Download' + '\\' + name + '第' + str(Begin) + "-" + str(End)+"话"
        totalpath = basicpath+str('\\第' + str(num) + '话')
        self.mkdir(totalpath)
        firsturl = url[:-5] 
        picbase = "http://pc.ihhmh.com/"
        for i in range(1,20):
            totalurl = firsturl + str(i) + ".htm"
            print("begin find")
            try:
                pageresp = PyQuery(totalurl,encoding = "gbk")
                html = pageresp.text()
                html = html.split("\n")
                html = html[4][16:-3]
                html = html.split('"')[4][:-9]
                picurl = picbase + html
                print("pic found")
                if(not self.downloadpic(picurl, i , totalpath + '\\')):
                    break
            except:
                pass
        print(str(num)+"finished")

    def mainDownload(self,begin):
        """
        开始爬取
        :param mangaID: 漫画在风之动漫对应的编号
        :param Begin: 起始章节
        :param End: 结束章节
        """
        baseurl = "http://www.manmanju.com/"
        urllist,reslist = self.getList()
        print(urllist)
        actualbegin = begin - 461
        for i in range(actualbegin,len(urllist)):
            self.downonehua(baseurl + urllist[i],i + 461,begin,len(urllist) + 461,"海贼王")

if __name__ == '__main__':
    MC = MangaCreeper()
    # MC.mainDownload(2, 930, 1050)
    MC.mainDownload(1047)
    # MC.downonehua("http://www.manmanju.com/comiclist/4/68741/1.htm",930,930,1000,"财神镇")