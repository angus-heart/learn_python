import zmail
import re
def get_my_mail():
    mail_server = zmail.server(username='python_wanmen@163.com',
                               password='XZZYKNOGGJTJOFHL',
                               pop_host='pop.163.com'
                               )
    mymail = mail_server.get_latest()
    zmail.show(mymail)
    #获取邮箱里的主体内容
    subject = mymail['Subject']
    #正则提取发件人
    patt  = r'<(.*?)>'
    email_from =  re.findall(string=mymail['From'],pattern=patt)[0]

    text = mymail['Content_text'][0].replace('\r','').replace('\n','').replace('&nbsp','')

    print(subject,email_from,text)
    return subject,email_from,text


