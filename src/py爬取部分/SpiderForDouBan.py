# Use this program to get data from DouBan.
# By fengh16, 17.10.25

import requests
from bs4 import BeautifulSoup
import random
import time
import re

Windows = True

s = requests.Session()
s.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'}


# Wait for some time in case that the spider been caught.
def sleep_sometime(seconds = 1):
    num = random.normalvariate(seconds, 1)
    while num * 2 <= seconds:
        num = random.normalvariate(seconds, 1)
    time.sleep(num)


login = s.get("https://accounts.douban.com/login")
sleep_sometime(5)
logindata = {'source':'None','redir':'https:/www.douban.com','form_email':'fengh16@163.com','form_password':'password','login':'登陆'}
logindata['captcha-id']='JksXFdvxVXmXt6XpHvHKlmi9:en'
logindata['captcha-solution']='history'
loginreturn = s.post("https://accounts.douban.com/login", logindata)
if Windows:
    print(loginreturn.text)
    logindata['captcha-id'] = input()
    logindata['captcha-solution'] = input()
    loginreturn = s.post("https://accounts.douban.com/login", logindata)

# For Windows:
if Windows:
    a = open(r"C:\Users\Koala_FH\Desktop\b.txt")
    b = a.read()
    soup = BeautifulSoup(b, 'html.parser', from_encoding='utf-8')
    result = soup('div')
    tags = soup.find_all('a', class_="item")
    no = 0
    # get = False
else:
    # For linux(Ubuntu Server on Tencent):
    a = open("/home/ubuntu/spider/url.txt")
    b = a.read()
    tags = b.split("\n")
    no = 0

startfrom = "https://movie.douban.com/subject/1292052/comments?start=43664&limit=20&sort=new_score&status=P&percent_type="
started = True
# 如果需要重新继续开始，改成False
for tag in tags:
    if Windows:
        ansnow0 = tag.get("href")
    else:
        ansnow0 = tag
    if ansnow0 == '':
        continue
    ansnow = ansnow0 + "comments?status=P"
    # if ansnow == "https://movie.douban.com/subject/26387939/":
    #     get = True
    # if not get:
    #     continue
    # c = open(r"C:\Users\Koala_FH\Desktop\textans.txt", 'a+')
    # c.write(ansnow + '\n')
    if Windows:
        # For Windows:
        filepath = "C:\\Users\\Koala_FH\\Desktop\\moviedata\\"
        adder = "data\\"
    else:
        # For linux(Ubuntu Server on Tencent):
        filepath = "/home/ubuntu/spider/moviedata/"
        adder = "data/"
    no = no + 1
    # 如果需要从某一个开始，则修改下面的no
    if no <= 5:
        continue
    if no > 50:
        break
    print(no)
    firstwrite = True
    if not started:
        started = True
        ansnow = startfrom
        firstwrite = False
    print(ansnow)
    num = 1
    while num != 200:
        try:
            b = s.get(ansnow)
            num = b.status_code
            print(num)
            if num == 200:
                if len(b.text) < 500:
                    num = 1
                    continue
                b = b.text
                print("OK")
                result = BeautifulSoup(b, 'html.parser', from_encoding='utf-8')
                print(filepath + adder + str(no) + ".txt")
                if firstwrite:
                    file = open(filepath + adder + str(no) + ".txt", 'w', encoding="utf-8")
                    print("Wrote!")
                else:
                    file = open(filepath + adder + str(no) + ".txt", 'a+', encoding="utf-8")
                    print("WroteAdd!")
                file.write(ansnow + "\n")
                file.write(b)
                file.close()
                firstwrite = False
                tags = result.find_all('a', class_="next")
                print(tags)
                if len(tags) > 0:
                    print("Bigger")
                    num = 1
                    ansnow = ansnow0 + "comments" + tags[0].get("href")
                    print(ansnow)
                sleep_sometime(0.2)
            else:
                sleep_sometime(6)
        except:
            sleep_sometime(6)
    # c.close()





logindata['captcha-id']='JBjVFEvuGHCMlKeiHSqA235u:en'
logindata['captcha-solution']='garden'
loginreturn = s.post("https://accounts.douban.com/login", logindata)