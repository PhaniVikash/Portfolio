import smtplib , ssl

host='smtp.gmail.com'
port=465

username='phanivikash@gmail.com'
password='cnrq wzsf pyuo dodq'
receiver='phanivikash2@gmail.com'
mess='''\
Subject : Testing
Hi ,SMTP Testing
'''

content=ssl.create_default_context()

with smtplib.SMTP_SSL(host,port,context=content) as server:
    server.login(user=username,password=password)
    server.sendmail(username,receiver,msg=mess)