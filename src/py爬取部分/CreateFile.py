from bs4 import BeautifulSoup

names = {}
scores = {}
# �����֮ǰ�����ڶ�ȡ�����۵�ʱ�򱣴��ڱ��ص�Դ���ļ���ʹ��������ȡ������Ӱ�����Ƶ�

# �пո�ʲô���ر𷳣�Ҳ�����Ҷ��Ŵ��ڲ������ˣ�ֱ�Ӵ��tsv��ʽ��ʡ��~ͬʱҲ����һ��csv��
outmovietsv = open("C:\\Users\\Koala_FH\\Desktop\\movie.tsv", "w", encoding="utf-8")
outmoviecsv = open("C:\\Users\\Koala_FH\\Desktop\\movie.csv", "w", encoding="utf-8")
outusertsv = open("C:\\Users\\Koala_FH\\Desktop\\user.tsv", "w", encoding="utf-8")
outusercsv = open("C:\\Users\\Koala_FH\\Desktop\\user.csv", "w", encoding="utf-8")
outtsv = open("C:\\Users\\Koala_FH\\Desktop\\out.tsv", "w", encoding="utf-8")
valuetsv = open("C:\\Users\\Koala_FH\\Desktop\\value.tsv", "w", encoding="utf-8")

stdr = "C:\\Users\\Koala_FH\\Desktop\\moviedata\\"
str2 = "C:\\Users\\Koala_FH\\Desktop\\moviedata\\data\\t"

map = {}

outtsv.write("ori\t")

for i in range(2699):
    p = open(stdr + str(i + 1) + ".txt", encoding="utf-8").read()
    temp = p.split("\n")[0]
    soup = BeautifulSoup(p, 'html.parser', from_encoding='utf-8')
    c = soup.find_all("strong", class_="rating_num")[0].text
    names[i] = temp
    scores[i] = c
    outmovietsv.write(names[i] + "\t" + scores[i] + "\n")
    outmoviecsv.write('' + names[i] + ',' + scores[i] + "\n")

    soup = BeautifulSoup(open(str2 + str(i + 1) + ".txt", encoding="utf-8").read(),'html.parser', from_encoding='utf-8')
    t = soup.find_all("comment")
    for tt in t:
        outusertsv.write(names[i] + "\t" + tt.find("name").text + "\t" + tt.find("score").text + "\n")
        outusercsv.write(names[i] + "," + tt.find("name").text + "," + tt.find("score").text + "\n")
        if map.get(tt.find("name").text):
            map[tt.find("name").text].append(i)
        else:
            map[tt.find("name").text] = [ names[i] ]
    print(i)


for i in range(2698):
    outtsv.write(names[i] + "\t")


outtsv.write(names[2698] + "\nscore\t")
for i in range(2698):
    outtsv.write(scores[i] + "\t")


outtsv.write(names[2698])

ans2 = []

for i in range(2699):
    ans = []
    for j in range(2699):
        ans.append(0)
    ans2.append(ans)

for i in map:
    for j in map[i]:
        for p in map[i]:
            if j == p:
                continue
            ans2[int(j)][int(p)] += 1

valuetsv.write("source\ttarget\tvalue")

for i in range(2699):
    for j in range(2699):
        if ans2[i][j]:
            valuetsv.write("\n" + i + "\t" + j + "\t" + ans2[i][j])