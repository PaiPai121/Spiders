import requests
import re
import time

from pyquery import PyQuery as pq
class MangaCreeper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
        }

    def get_one_page(self,url,headers):

        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response
        else:
            self.get_one_page(url,headers)


    def download(self,url):
        pass
    def downloadpic(self,url):
        response = self.get_one_page(url,self.headers)
        html = response.text
        doc = pq(html)
        td_links = doc('td a')
        links = [l.attr("href") for l in td_links.items()]
        self.mkdir("res")
        for link in links:
            self.download(link)
        # print(realtitle)
        # 打印出这些链接
        # for link in projection_links:
        #     print(link)
        
        


if __name__ == '__main__':
    url = "https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm#top"
    MC = MangaCreeper()
    MC.downloadpic(url)
