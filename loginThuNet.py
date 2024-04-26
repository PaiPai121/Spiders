import requests


class Loger:
    def __init__(self) -> None:
        pass
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.requestSession = requests.Session()
    def logOut(self):
        # 断网
        url = "http://net.tsinghua.edu.cn/do_login.php"
        data = {"action": "logout"}
        self.requestSession.post(url,data=data,headers=self.headers)
    def logIn(self):
        # 联网
        url = "http://net.tsinghua.edu.cn/do_login.php"
        data = {"action": "login",
                "username": "zhangzk19",
                "password": "{MD5_HEX}7d41ddc2d022546ed3ae37267067ae60",
                "ac_id": "1"}
        self.requestSession.post(url,data=data,headers=self.headers)

if __name__ == "__main__":
    L = Loger()
    
    L.logIn()