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
sleep_sometime()
logindata = {'source':'None','redir':'https%3A%2F%2Fwww.douban.com','form_email':'fengh16@163.com','form_password':'password','login':'登陆'}
loginreturn = s.post("https://accounts.douban.com/login", logindata)
while True:
    soup = BeautifulSoup(loginreturn.text, 'html.parser')
    img = soup.findAll('img', id="captcha_image")
    if len(loginreturn.text) < 500:
        sleep_sometime()
        continue
    if len(img) <= 0:
        break
    print("Please Open following url and input the captcha:")
    print(img[0].get("src"))
    logindata['captcha-id'] = re.findall("id=([\w:]+)", img[0].get("src"))[0]
    logindata['captcha-solution'] = input("Input the captcha: ")
    print(logindata)
    loginreturn = s.post("https://accounts.douban.com/login", logindata)


print("Login Success!")
# For Windows:
if Windows:
    a = open(r"C:\Users\Koala_FH\Desktop\b.txt")
    b = a.read()
    soup = BeautifulSoup(b, 'html.parser')
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
    ansnow = ansnow0 + "reviews"
    # if ansnow == "https://movie.douban.com/subject/26387939/":
    #     get = True
    # if not get:
    #     continue
    # c = open(r"C:\Users\Koala_FH\Desktop\textans.txt", 'a+')
    # c.write(ansnow + '\n')
    if Windows:
        # For Windows:
        filepath = "C:\\Users\\Koala_FH\\Desktop\\reviewdata\\"
        adder = "data\\"
    else:
        # For linux(Ubuntu Server on Tencent):
        filepath = "/home/ubuntu/spider/reviewdata/"
        adder = "data/"
    no = no + 1
    # Controls where to start
    if no <= 0:
        continue
    if no > 5000:
        break
    print("Now Film No.")
    print(no)
    firstwrite = True
    if not started:
        started = True
        ansnow = startfrom
        firstwrite = False
    print("Url that will be visited:")
    print(ansnow)
    num = 1
    while num != 200:
        try:
            b = s.get(ansnow)
            num = b.status_code
            print("Return Code:")
            print(num)
            if num == 200:
                if len(b.text) < 500:
                    num = 1
                    continue
                b = b.text
                print("OK")
                result = BeautifulSoup(b, 'html.parser')
                if firstwrite:
                    file = open(filepath + adder + str(no) + ".txt", 'w', encoding="utf-8")
                    tar = open(filepath + adder + "t" + str(no) + ".txt", 'w', encoding="utf-8")
                    print("Wrote!")
                else:
                    file = open(filepath + adder + str(no) + ".txt", 'a+', encoding="utf-8")
                    tar = open(filepath + adder + "t" + str(no) + ".txt", 'a+', encoding="utf-8")
                    print("WroteAdd!")
                file.write(ansnow + "\n")
                file.write(b)
                c = result.find_all("div", class_="main review-item")
                for d in c:
                    try:
                        name = d.find("a", class_="author").find('span').text
                        score = d.find_all("span")[1].get("title")
                        textinput = "<comment><name>" + str(name) + "</name><score>" + str(score) + "</score></comment>"
                        tar.write(textinput)
                    except Exception as e:
                        tempfile = open("a.log", 'a+')
                        tempfile.write(e)
                        tempfile.close()
                        print(e)
                tar.close()
                file.close()
                firstwrite = False
                tags = result.find_all('span', class_="next")
                if len(tags) > 0 and len(tags[0].find_all('a')) > 0:
                    print("Bigger")
                    num = 1
                    ansnow = ansnow0 + "reviews" + tags[0].find('a').get("href")
                    print("Next Page:")
                    print(ansnow)
                sleep_sometime(0.2)
            else:
                sleep_sometime(6)
        except:
            sleep_sometime(6)
    # c.close()
