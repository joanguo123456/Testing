#coding:utf-8
from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
from time import sleep
from Util.EconfigDemo import OperateEconfig

class SendEmail:
    global EmailServer,EmailUser,Password
    global sender,addresser

    oper_config = OperateEconfig('email.ini')
    EmailServer = oper_config.read_config('link','Emailserver')
    EmailUser = oper_config.read_config('link','User')
    Password = oper_config.read_config('link','Password')
    sender = oper_config.read_config('send','sender')
    addressers = oper_config.read_section('addressed')
    addresser = oper_config.get_addkey(addressers)
    def __init__(self,pass_count,fail_count):
        self.send = self.send_mail(pass_count,fail_count)
    #连接邮箱
    def send_mail(self,pass_count,fail_count):
        # 此句用来消除ssl证书错误，exchange使用自签证书需加上
        BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
        cred = Credentials(EmailUser, Password)
        print(cred)
        mailconfig = Configuration(server=EmailServer, credentials=cred, auth_type=NTLM)
        account = Account(primary_smtp_address=sender, config=mailconfig, autodiscover=False, access_type=DELEGATE)
        #message = MIMEMultipart()
        sleep(1)
        pass_count = float(pass_count)
        fail_count = float(fail_count)
        all = pass_count+fail_count
        pass_rate = "%.2f%%" % (pass_count/all*100)

        mbody = '本次运行接口%s个，其中通过个数为%s个，失败个数为%s个，通过率为%s。' %(all,pass_count,fail_count,pass_rate)
        m = Message(
            account = account,
            subject = "测试邮件", #邮件主题
            body = HTMLBody(mbody),
            to_recipients = addresser
            )
        m.send()
        print(cred)


if __name__ == "__main__":
    SendEmail().send_mail(6,6)


