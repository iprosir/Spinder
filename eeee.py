import requests
import re
import csv
import time

headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36","Referer":"https://www.dytt8.net/"}
proxy={"http":"113.140.1.82:53281","http":"115.221.127.171:808"}

movies=[]
for page in range(1,31):
    url="https://www.dytt8.net/html/gndy/dyzz/list_23_"+str(page)+".html"
    time.sleep(2)
    html=requests.get(url,headers=headers,proxies=proxy)
    html.encoding="gb2312"
    detail_list=re.findall('<a href="(.*)" class="ulink"',html.text)   #外双内单引号的问题,取得电影短网址
    # print(detail_list)

    for m in detail_list:
        movie_detail_url="https://www.dytt8.net"+m  #拿到电影的链接
        # print(movie_detail_url)
        html_movie=requests.get(movie_detail_url)
        html_movie.encoding="gb2312"
        movie_detail_tit=re.findall('<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>',html_movie.text) #获取电影的名称
        ftp=re.findall('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>',html_movie.text)   #获取电影下载地址
        movies.append([movie_detail_tit,movie_detail_url,ftp])
        # print(movie_detail_tit,movie_detail_url,ftp)

    with open("./movie/dytt.csv","w",newline="") as fp:
        write_flie = csv.writer(fp)
        head = ["电影名称", "电影网址", "下载地址"]
        write_flie.writerow(head)
        for rows in movies:
            write_flie.writerow(rows[0],rows[1],rows[2])


