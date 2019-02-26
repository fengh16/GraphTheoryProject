from bs4 import BeautifulSoup

def DealWithFile(fromfile, targetfile):
    tar = open(targetfile, 'w', encoding='utf-8')
    a = open(fromfile, encoding='utf-8')
    b = a.read()
    soup = BeautifulSoup(b, 'html.parser', from_encoding='utf-8')
    c = soup.find_all("div", class_="comment")
    for d in c:
        name = d.find("span", class_="comment-info").find("a").text
        score = d.find("span", class_="comment-info").find_all("span")[0].get("title")
        vote = d.find("span", class_="votes").text
        textinput = "<comment><name>" + name + "</name><score>" + score + "</score><vote>" + vote + "</vote></comment>"
        tar.write(textinput)
    tar.close()

fromf = r'C:\Users\Koala_FH\Desktop\moviedata\data\2.txt'
tarf = r'C:\Users\Koala_FH\Desktop\moviedata\data\t2.txt'

DealWithFile(fromf, tarf)