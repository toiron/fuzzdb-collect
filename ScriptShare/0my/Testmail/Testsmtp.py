'''
smtp验证邮箱账号密码，163、QQ登邮箱的邮箱密码需要输入第三方授权码，自己搭建的邮箱服务则输入密码即可。
'''
#enconding=utf-8
import smtplib

def check(email, password):
    try:
        email = email
        password = password
        smtp_server = "smtp.163.com"
        server = smtplib.SMTP(smtp_server)
        # a = server.set_debuglevel(1)
        # print(a) 打印调试信息
        server.login(email, password)
        #print('Messages: %s. Size: %s' % server.s())
        print(email+": successful")
    except Exception as e:
        print(email+"：fail")
        print(e)


if __name__ == '__main__':
    f = open("pop.txt", "r+")
    d = f.readlines()
    f.close()
    for line in d:
        line = line.strip()
        # mail = line.split(":")[0]
        # pwd = line.split(":")[1]
        a = line.split(":")
        check(a[0], a[1])
        print("*"*9)