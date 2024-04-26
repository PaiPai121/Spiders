import requests
import time
from pyquery import PyQuery as pq


class CpolarCreeper:
    def __init__(self,url = r"https://zfile.cosersets.com/api/list/1?path=%2F"):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.url = url
        self.requestSession = requests.Session()
        self.login()

    def get_one_page(self,url):
        """
        :param url: 目标地址
        :return: 返回html
        """
        def getPage(url):
            time.sleep(0.1)
            response = self.requestSession.get(url,headers = self.headers)
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
    
    def login(self):
        url = r"https://dashboard.cpolar.com/login"
        data = {
            "login": "zhangzk19@mails.tsinghua.edu.cn",
            "password": "1qaz2wsx",
        }
        self.requestSession.post(url = url,headers = self.headers,data=data) # 这里我有了登录的cookie

    def getStatus(self):
        self.login()
        headers = self.headers
        headers["referer"] = "https://dashboard.cpolar.com/get-started"
        url = r"https://dashboard.cpolar.com/status"
        response = self.requestSession.get(url = url,headers = headers)
        doc = pq(response.text)
        table = doc(".table table-sm")
        resurl = doc('th a').text()
        resurl = resurl.split(' ')
        return resurl
if __name__ == "__main__":
    url = r"https://www.cpolar.com/"
    cc = CpolarCreeper(url)
    url = cc.getStatus()
    print(url)