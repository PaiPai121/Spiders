from email import message
from email.mime import text
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

## 遵守SMTP协议

from Mailhosters import*

class MailSender(hosters):
    """hoster中只有init方法保存了邮箱地址、授权码"""
    def __init__(self) -> None:
        super().__init__()
        self.mm = MIMEMultipart('related')
    def addMailHeader(self,title = "Python 邮件测试"):
        """头部内容设置"""
        # 主题
        subject_content = title
        self.mm["From"] = self.mail_sender
        self.mm["To"] = ','.join(self.mail_receivers)
        self.mm["Subject"] = Header(subject_content,'utf-8')
    
    def addContent(self,text = "just for test"):
        body_content = text
        message_text = MIMEText(body_content,"plain","utf-8")
        self.mm.attach(message_text)

    def addPic(self,path):
        image_data = open(path,'rb')
        message_image = MIMEImage(image_data.read())
        image_data.close()
        self.mm.attach(message_image)

    def addAttachment(self,path,info = ""):
        atta = MIMEText(open('sample.xlsx','rb').read(),'base64','utf-8')
        atta['Content-Disposition'] = ""
        self.mm.attach(atta)

    def sendMail(self):
        stp = smtplib.SMTP()

        stp.connect(self.mail_host,25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        # stp.set_debuglevel(1)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        stp.login(self.mail_sender,self.mail_license)
        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        stp.sendmail(self.mail_sender, self.mail_receivers, self.mm.as_string())
        print("mail sent")
        stp.quit()

if __name__ =="__main__":
    MS = MailSender()
    MS.addMailHeader()
    MS.addContent()
    MS.addPic("test.jpg")
    MS.sendMail()