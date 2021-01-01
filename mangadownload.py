import requests
import re
import time

from bs4 import BeautifulSoup



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
        def getPath(i,res):
            basicPath = 'http://www-mipengine-org.mipcdn.com/i/p'
            basicPathEnd = '.manhuapan.com/'
            return basicPath + str(i) + basicPathEnd + res

        pattern = re.compile('var mhurl="(.*)";var\sUrl=')
        pattern2 = re.compile('var mhurl1="(.*)"')#检测是否到最后一页

        response = self.get_one_page(url,self.headers)
        html = response.text
        result = re.findall(pattern, html)
        if not result:
            return False
        # path = path1 + result[0]
        i=1
        path = getPath(i,result[0])
        print(path)
        response = self.get_one_page(path,headers = self.headers)

        while (response == None) and path and i < 25:
            time.sleep(1)
            path = getPath(i, result[0])
            response = self.get_one_page(path, headers=self.headers)
            i += 1
        if response == None:
            print("download page"+str(num)+'Failed \n')
        else:
            print("successfully download page"+str(num)+'\n')
        with open(filepath +'第' + str(num) +'张.jpg','wb') as fw:
            fw.write(response.content)

        result2 = re.findall(pattern2,html)

        if result2:
            return True#有下一页
        else:
            return False#没有下一页


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

    def mainDownload(self,mangaID,Begin,End):
        """
        开始爬取
        :param mangaID: 漫画在风之动漫对应的编号
        :param Begin: 起始章节
        :param End: 结束章节
        """
        basicurl = 'https://www.fzdm.com/manhua/'+str(mangaID)+'/'
        name = self.getName(basicurl)
        for i in range(Begin,End):
            url = basicurl + str(i)
            self.downwords(url,i,Begin,End,name)


if __name__ == '__main__':
    MC = MangaCreeper()
    MC.mainDownload(2, 901, 1000)
