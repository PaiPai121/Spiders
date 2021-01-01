import re
import time
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Set-Cookie':""
}
url = "http://www.biquge.info/12_12313/5508348.html"
session = requests.Session()

from pyquery import PyQuery as pq

path = r'D:\BiQuGe\盖世双谐.txt'

f = open(path,mode = 'w+',encoding= "utf8")

def getContent(url,session,title):
    response = session.get(url,headers=headers)
    response.encoding = 'utf8'
    html = response.text
    doc = pq(html)

    realtitle = doc('.bookname h1').text()
    
    print("内容标题：",doc('.bookname h1').text())
    if title == realtitle:
        print("download success")
        return doc
    else:
        print("Error occured")
        time.sleep(0.2)
        return getContent(url,session,title)

def get_one_page(url,f,session,title):

    doc = getContent(url,session,title)

    f.write("#")
    f.write(doc('.bookname h1').text())# 标题
    f.write('\n\n\t')
    c = doc('#content').text()
    c = c.replace('\n\n','\n\n\t')
    f.write(c) # 内容
    f.write('\n')
    f.write('\n')
    # print("download success")
    # # 获取下一页url
    # bottem = doc('.bottem')('a')
    # i = 0
    # for a in bottem.items():    
    #     nexturl = a.attr('href')
    #     if a.text() == "下一章":
    #         return nexturl
    return title,html
# i = 2
# finishUrl = 'http://www.biquge.info/12_12313/'
# while not url == finishUrl:#i > 0:
#     #i -= 1
#     url = get_one_page(url,f,session)
baseUrl = r'http://www.biquge.info/12_12313/'
response = session.get(baseUrl,headers=headers)
response.encoding='utf8'
html = response.text
doc = pq(html)
dds = doc('dl')('dd')
i = 0
for dd in dds.items():
    i += 1
    # print(dd('a').attr('href'))
    print("目录名称：",dd('a').text())
    newurl = baseUrl + dd('a').attr('href')
    title,html = get_one_page(newurl,f,session,dd('a').text())
    if title == dd('a').text():
        print("download success")
    else:
        print("Error occured")
        print(newurl,'\n')
        print(html)
    time.sleep(0.5)
print(i)