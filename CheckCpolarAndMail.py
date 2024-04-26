from sys import winver
from pyquery import text
from SpiderForCpolar import CpolarCreeper
import time
import schedule


from SendMails import MailSender

def SendChangedMail(urls):
    MS = MailSender()
    MS.addMailHeader("Cpolar 地址变更 检查时间: " + time.ctime(time.time()))
    content = "Cpolar地址已变更\n"
    for u in urls:
        content += "new url: \n" + u +" \n"
    MS.addContent(content)
    # MS.addPic("test.jpg")
    MS.sendMail()
    del MS

lasturls = []

def checkCpolar():
    global lasturls
    print("begin checking url")
    try:
        cc = CpolarCreeper()
        # 获取当前的cpolar隧穿url
        urls = cc.getStatus()
        print("checked successfully")
    except:
        print("check failed")
    if urls == lasturls:
        print('url not change')
    else:
        saveLastUrl()
        print('url changed')
        try:
            SendChangedMail(urls)
            print("mail send successfully")
        except:
            print('mail send failed')
        lasturls = urls
    del cc

def readLastUrl():
    global lasturls
    with open('cpolarUrlSaved.txt',"r",encoding="utf-8") as f:
        lasturls = f.read().split('\n')[:-1]

def saveLastUrl():
    global lasturls
    with open('cpolarUrlSaved.txt',"w",encoding="utf-8") as f:
        for u in lasturls:
            f.write(u + '\n')

if __name__ == "__main__":
    readLastUrl()
    schedule.every().hour.do(checkCpolar) 
    while True:
        schedule.run_pending()   #run_pending：运行所有可以运行的任务
