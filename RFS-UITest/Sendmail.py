#-*- coding: utf-8 -*-
#encoding = utf-8

import time 
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import sys
import os.path
reload(sys)
sys.setdefaultencoding('utf-8')


mailto_list = ['xxx@qq.com']
mail_host = "smtp.exmail.qq.com"
mail_user = "username"
mail_pass = "password"
# mail_postfix = "sogaa.net"


def send_mail(open_file, attfile1, attfile2):
	soup = BeautifulSoup(open(open_file, 'rb'), "html.parser")
	body = soup.find("body")
	runPassRate = body.find("td").string
	PassRate = runPassRate.split(" ")[3]
	today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	detailTime - time.strftime('%H:%M:%S', time.localtime(time.time()))
	todaytime = today + '00:00:00'
	selectres = todaytime
	send_header = "[速加网][上线前测试环境][主业务流程自动化用例执行批跑报告]- ".encode("utf-8") + today + " " + detailTime + " " + PassRate
	# me = "[速加网][上线前测试环境][主业务流程自动化用例执行批跑报告]".encode("utf-8") + "<" + mail_user + "@" + mail_postfix + ">"
	msg = MIMEMultipart()
	msg['Subject'] = send_header
	msg['From'] = mail_user
	msg['To'] = ";".join(mailto_list)

	fp = open(r'E:/robotframework/logs/log.html', "r")
	# fp = open(open_file, "r")_
	content = fp.read()
	msg.attach(MIMEText(content, _subtype = 'html', _charset = 'utf-8'))
	fp.close()

	#log report
	att1 = MIMEText(open(r'E:/robotframework/logs/log.html', 'rb').read(), 'base64', 'gb2312')
	# att1 = MIMEText(open(attfile1, 'rb').read(), 'base64', 'gb2312')
	att1["Content-Type"] = 'application/octet-stream'
	att1["Content-Disposition"] = 'attachment; filename="report.html"'
	msg.attach(att1)

	# result report
	att2 = MIMEText(open(r'E:/robotframework/logs/report.html', 'rb').read(), 'base64', 'gb2312')
	# att2 = MIMEText(open(attfile2, 'rb').read(), 'base64', 'gb2312')
	att2["Content-Type"] = 'application/octet-stream'
	att2["Content-Disposition"] = 'attachment; filename="log.html"'
	msg.attach(att2) 
	
	try:
		server = smtplib.SMTP()
		server.connect(mail_host)
		server.login(mail_user,mail_pass)
		server.sendmail(me, mailto_list, msg.as_string())
		server.close()
		return True
	except Exception, e:
		print str(e)
		return False

if __name__ == '__main__':  
    if send_mail(r'E:/robotframework/logs/log.html', r'E:/robotframework/logs/log.html', r'E:/robotframework/logs/report.html'):
        print u"发送成功"
    else:  
        print u"发送失败"