# -*- coding: UTF-8 -*-#
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import *

report_dir = "C:\\Users\\ancey\\PycharmProjects\\myproject\\testReport"  # 定义测试报告目录

def newReport():


    replist = os.listdir(report_dir)    # 获取目录下的所有文件、文件夹保存为列表
    replist.sort(reverse=False)     # 根据名称进行顺序排序
    last_report = os.path.join(report_dir,replist[-1])  # 合并路径，得到最新报告的绝对路径
    return last_report

def sendEmail(test_report):

    report = open(test_report,'rb')
    mail_att = report.read()
    report.close()

    file_att = MIMEText(mail_att,'base64','utf-8')
    file_att['Content-Type'] =content_type
    file_att['Content-Disposition'] = content_disposition

    context = MIMEText(mail_att,'html','utf-8')

    msg = MIMEMultipart('mixed')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = e_sender
    msg['To'] = ';'.join(e_accepter)      # 收件人是列表，需要join;
    print msg['To']

    msg.attach(file_att)    # 添加附件到邮件
    msg.attach(context)      # 添加正文到邮件

    try:
        smtp = smtplib.SMTP()
        smtp.connect(e_service)
        smtp.login(e_sender,psw)
        smtp.sendmail(e_sender,e_toaddr,msg.as_string())
        smtp.quit()
        print u'发送成功'
    except smtplib.SMTPException:
        print u'发送失败'

if __name__ =='__main__':

    sendEmail(newReport())
