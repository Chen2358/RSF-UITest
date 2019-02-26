#-*- coding: utf-8 -*-
#encoding = utf-8


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 邮件头
from_addr = 'username'
password = 'password'
to_addr = 'xxx@qq.com'
smtp_server = 'smtp.exmail.qq.com'

# 创建一个带附件的实例
msg = MIMEMultipart()

def send_mail(attfile11, attfile2):
	msg['From'] = _format_addr(from_addr)
	msg['To'] = _format_addr(to_addr)
	msg['Subject'] = Header('[主业务流程自动化用例执行批跑报告]' , 'utf-8').encode()



	#构造附件1
	att1 = MIMEText(open('E:/robotframework/logs/report.html', 'rb').read(), 'base64', 'gb2312')
	att1["Content-Type"] = 'application/octet-stream'
	att1['Content-Disposition'] = 'attachment; filename="report.html"'
	msg.attach(att1)

	#构造附件2
	att2 = MIMEText(open('E:/robotframework/logs/log.html', 'rb').read(), 'base64', 'gb2312')
	att2["Content-Type"] = 'application/octet-stream'
	att2['Content-Disposition'] = 'attachment; filename="log.html"'
	msg.attach(att2)

	# 发送邮件
	try:
		server = smtplib.SMTP()
		server.connect(smtp_server, 465)
		server.login(from_addr, password)
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		server.close()
		return True
	
	except Exception, e:
		print str(e)
		return False

if __name__ == '__main__':
	if send_mail('E:/robotframework/logs/report.html', 'E:/robotframework/logs/log.html'):
		print("sucess")
	else:
		print("failed")
