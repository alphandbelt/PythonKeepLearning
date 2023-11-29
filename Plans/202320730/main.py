"""
        1.  发送邮件
        qq邮箱

        准备工作
        qq邮箱的例子
        获取到自己的授权码 smtp

        a. 发送普通格式的邮件
        b. 带有格式的邮件
            -改变字体的大小，颜色，添加表格...
        c. 带有图片的邮件
            - 单个图片，两个图片，多个图片...
            -                  for 循环 （有特征）
        d. 带有附件的邮件
            - 单个附件，两个附件，多个附件...
            -                  for 循环

        9:50 开始




"""
import smtplib
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from info import Info
import os
import shutil
import psutil # 分区的 内存 cpu



sender_user = Info.sender_user
recv_user = Info.recv_user
auth_password = Info.auth_password
mail_host = 'smtp.qq.com'  # qq邮箱邮件服务器
mail_port = 465  # 端口


def email1():
    #  发送普通邮件
    print(sender_user, recv_user)
    msg = '这是一个测试的邮件'
    try:

        # dict['key']= 'value'
        message = MIMEText(msg, 'html', 'utf-8')
        message['From'] = f'{sender_user} <{sender_user}>'
        message['To'] = Header(recv_user, 'utf-8')
        subject = '测试邮件'
        message['Subject'] = subject
        smtp_obj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtp_obj.login(sender_user, auth_password)
        smtp_obj.sendmail(sender_user, recv_user, message.as_string())
        print("mail send ok.")
    except Exception as e:
        print(e)


def email2():
    # 发送html格式的邮件
    # 浏览器 f12
    # html  <h1></h1>

    # 表格
    # 改变字体的颜色
    # 改变自体的大小

    # 正文标题（大字号）  测试邮件
    # 正文（小字号）    这是邮件内容

    # 1. 获取到硬盘信息
    # 2. 判断硬盘的使用容量是否超过某个值，90%
    # 3. 发送邮件警告⚠️
    # 4. 邮件的内容:
    #       - 每个磁盘的使用详情 表格的形式。

    msg = '这是邮件内容'
    msg_html = f"<h1>邮件告警</h1> <p>{msg}</p>"
    content =[]
    for d in data:
        f = f"<tr align=center><td>{d[1]}</td><td>{d[0]}%</td></tr>"
        content.append(f)

    table = f'<table border=1 bgcolor=F3E2A9 width=61%>' \
            f'<tr align=center><td>磁盘分区统计</td></tr>' \
            f'</table>' \
            f'<table border=1 bgcolor=CCCCCC width=61%>' \
            f'<tr align=center><th>挂载点</th><th>已使用容量</th></tr>'

    table = table + "".join(content) + '</table>'
    table = msg_html + table

    try:
        message = MIMEText(table, 'html', 'utf-8')
        # message['From'] = Header(sender_user, 'utf-8')
        message['From'] = f'{sender_user} <{sender_user}>'  # 发件人
        message['To'] = Header(recv_user, 'utf-8')  # 收件人
        message['Subject'] = '测试邮件'

        smtp_obj = smtplib.SMTP_SSL(mail_host, mail_port) # https
        # smtp_obj.connect(host=mail_host, port=mail_port)

        # 登录
        # params: 发件人的邮箱 授权码
        smtp_obj.login(sender_user, auth_password)

        #
        smtp_obj.sendmail(sender_user, recv_user, message.as_string())
        print("mail send ok.")
    except Exception as e:
        print(e)


def email3():

    # 带有图片的

    # 树🌲
    #      |
    #     /  \
    #    /    \
    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = f'{sender_user} <{sender_user}>'
    msgRoot['To'] = Header(recv_user, 'utf-8')
    msgRoot['Subject'] = Header('Python 发送 邮件测试', 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    # '' "" """
    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p>图片演示：</p>
    """




    # <p><img decoding="async" src="cid:image1" width="512" height="512"></p>
    #     <p><img decoding="async" src="cid:image2" width="512" height="512"></p>

    mail_multi = ''
    for i in range(0, 10):
        # index
        mail_multi += f'<p><img decoding="async" src="cid:image{i}" width="512" height="512"></p>'
    mail_msg += mail_multi
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # # 指定图片为当前目录
    # msgImage = MIMEImage(open('test.png', 'rb').read())
    # # 定义图片 ID，在 HTML 文本中引用
    # msgImage.add_header('Content-ID', '<image1>')
    # msgRoot.attach(msgImage)
    #
    # # 第二张图片
    # msgImage2 = MIMEImage(open('test2.png','rb').read())
    # msgImage2.add_header('Content-ID','<image2>')
    # msgRoot.attach(msgImage2)

    for i in range(0,10):
        msgMutiImage = MIMEImage(open(f'test{i}.png','rb').read())
        msgMutiImage.add_header('Content-ID',f'<image{i}>')
        msgRoot.attach(msgMutiImage)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(sender_user, auth_password)
        smtpObj.sendmail(sender_user, recv_user, msgRoot.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)

def email4():
    # create message object
    # 带有附件的邮件
    try:
        mgs_root = MIMEMultipart()
        # add in header
        # message['From'] = Header(sender_user)
        mgs_root['From'] = f'{sender_user} <{sender_user}>'
        mgs_root['To'] = Header(recv_user)
        mgs_root['Subject'] = Header('带附件的邮件📧')

        # attach message body as MIMEText

        body = '邮件正文，今天直播讲的是如何发送带有格式的邮件，和带有' \
               '图片的邮件，带有附件的邮件'

        mgs_root.attach(MIMEText(body, 'plain', 'utf-8'))


        filename = './TDDO.py'
        att_name = os.path.basename(filename)
        att = MIMEApplication(open(filename, 'rb').read(), _subtype="txt")
        att.add_header('Content-Disposition', 'attachment', filename=att_name)

        # subtype 附件的类型并不一定是文件的后缀。
        filename2 = "./test.png"
        att2_name = os.path.basename(filename2)
        att2 = MIMEApplication(open(filename2,'rb').read(),_subtype='png')
        att2.add_header('Content-Disposition','attachment',filename=att2_name)

        mgs_root.attach(att)
        mgs_root.attach(att2)

        # setup email server
        server = smtplib.SMTP_SSL(mail_host, mail_port)
        server.login(sender_user, auth_password)

        # send email and quit server
        server.sendmail(sender_user, recv_user, mgs_root.as_string())
        server.quit()
        print("ok")
    except Exception as e:
        print(e)

def get_disk_partitions():
    disk_info = []

    pds = psutil.disk_partitions()
    for pd in pds:
        # print(pd.mountpoint)
        use = shutil.disk_usage(pd.mountpoint)
        # print(f"use:{use}")
        use_percentage = use.used/use.total * 100.0
        # print(f"use_percentage:{use_percentage}%")
        tmp = (pd.mountpoint,format(use_percentage,'.0f'))
        disk_info.append(tmp)
    # print(disk_info)
    return disk_info


def send_mail5():

    r_info = None

    flag = False
    disks = get_disk_partitions()
    subject = ''

    for disk in disks:
        # (1,2)
        if float(disk[1]) > 90:
            r_info= disk
            disk_name = disk[0]
            subject = f'磁盘容量[{disk_name}]超过预定设置，遂发邮件进行警告通知'
            flag = True
    if flag:

        # send_mail


        #------磁盘分区统计--------------|
        #-------------------------------
        #|    磁盘名称  |   使用百分比    |
        #|      硬盘1   |     76%       |
        #|      硬盘2   |      95%      |

        msg = '磁盘分区信息'
        msg_html = f"<h1>磁盘使用容量告警</h1> <p>{msg}</p>"
        content = []
        for d in disks:
            f = f"<tr align=center><td>{d[0]}</td><td>{d[1]}%</td></tr>"
            content.append(f)

        table = f'<table border=1 bgcolor=F3E2A9 width=61%>' \
                f'<tr align=center><td>磁盘分区统计</td></tr>' \
                f'</table>' \
                f'<table border=1 bgcolor=CCCCCC width=61%>' \
                f'<tr align=center><th>挂载点</th><th>已使用容量</th></tr>'

        table = table + "".join(content) + '</table>'
        table = msg_html + table

        try:
            message = MIMEText(table, 'html', 'utf-8')
            # message['From'] = Header(sender_user, 'utf-8')
            message['From'] = f'{sender_user} <{sender_user}>'  # 发件人
            message['To'] = Header(recv_user, 'utf-8')  # 收件人
            message['Subject'] = subject

            smtp_obj = smtplib.SMTP_SSL(mail_host, mail_port)  # https
            # smtp_obj.connect(host=mail_host, port=mail_port)
            # 登录
            # params: 发件人的邮箱 授权码
            smtp_obj.login(sender_user, auth_password)
            #
            smtp_obj.sendmail(sender_user, recv_user, message.as_string())
            print("mail send ok.")

            return r_info
        except Exception as e:
            print(e)


def auto_alarm():
    # 重复发送邮件
    #
    handled = []
    while True:
        print("循环",time.time(),handled)
        disks = get_disk_partitions()
        for disk in disks:
            if float(disk[1]) > 90:
                if disk not in handled:
                    print("达到告警条件，发邮件告警")
                    handled.append(disk)
                    send_mail5()
                    # 触发告警的磁盘信息
                else:
                    print("此前已经有过这种情况，不再进行发送")

        time.sleep(10)


if __name__ == "__main__":
    #email2()
    #email3()
    #email4()
    #send_mail5()
    auto_alarm()
