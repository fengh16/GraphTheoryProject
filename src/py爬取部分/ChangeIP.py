# Use this program to get movie data from DouBan.
# By fengh16, 17.10.25

import requests
from bs4 import BeautifulSoup
import random
import time
import re

Windows = False
nowIPnum = 1

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


def ChangeIP(n = 1):
    while True:
        try:
            s.proxies = {}
            url = 'http://www.xicidaili.com/nn/1'
            res = s.get(url)
            res = res.text
            print(res)
            soup = BeautifulSoup(res, 'html.parser')
            ips = soup.findAll('tr')
            if n >= len(ips):
                n = 1
            for x in range(n, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                ip_temp = "http://" + tds[1].text + ":" + tds[2].text
                print(ip_temp)
                try:
                    s.proxies = {'http': ip_temp}
                    res = s.get("http://ip.chinaz.com/", timeout=3)
                    print(res.status_code)
                    if res.status_code == 200:
                        print(res.text)
                        soup = BeautifulSoup(res.text, 'html.parser', from_encoding="utf-8")
                        m = soup.find_all('dd', class_="fz24")
                        print(m)
                        if len(m) > 0 and tds[1].text == m[0].text:
                            print("OK")
                            print(tds[1].text)
                            return x
                except:
                    continue
            break
        except:
            continue


nowIPnum = ChangeIP()
while True:
    try:
        login = s.get("https://accounts.douban.com/login")
        sleep_sometime(3)
        logindata = {'source':'None','redir':'https:/www.douban.com','form_email':'fengh16@mails.tsinghua.edu.cn','form_password':'password','login':'登陆'}
        while True:
            loginreturn = s.post("https://accounts.douban.com/login", logindata)
            soup = BeautifulSoup(loginreturn.text, 'html.parser')
            img = soup.findAll('img', id="captcha_image")
            print(loginreturn.text)
            if len(loginreturn.text) < 500:
                nowIPnum = ChangeIP(nowIPnum)
                continue
            if len(img) <= 0:
                break
            print("Please Open following url and input the captcha:")
            print(img[0].get("src"))
            logindata['captcha-id'] = re.findall("id=([\w:]+)", img[0].get("src"))[0]
            logindata['captcha-solution'] = input("Input the captcha: ")
            loginreturn = s.post("https://accounts.douban.com/login", logindata)
        break
    except:
        continue

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
started = False
# If you've Got several data and want to continue, just change started to False
for tag in tags:
    nowIPnum = 1
    while True:
        try:
            if Windows:
                ansnow0 = tag.get("href")
            else:
                ansnow0 = tag
            if ansnow0 == '':
                continue
            ansnow = ansnow0 + "comments?status=P"
            if Windows:
                # For Windows:
                filepath = "C:\\Users\\Koala_FH\\Desktop\\moviedata\\"
                adder = "data\\"
            else:
                # For linux(Ubuntu Server on Tencent):
                filepath = "/home/ubuntu/spider/moviedata/"
                adder = "data/"
            no = no + 1
            # Get specific data in the following range
            if no <= 50:
                continue
            if no > 2800:
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
                        nowIPnum = ChangeIP()
                except:
                    nowIPnum = ChangeIP()
            break
        except:
            continue