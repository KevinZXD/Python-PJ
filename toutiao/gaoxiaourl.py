# -*- coding:utf-8 -*-
import urllib2
import re #正则
from bs4 import BeautifulSoup
import database
def get_video_url_range(begin,end):
    mysql_s = database.Mysql()
    for i in range(begin, end):
        url='http://www.budejie.com/'+str(i)
	print(url)
        try:
            req = urllib2.Request(url) #请求页面 # 加一个键值对，针对服务器的反爬机制
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
            html = urllib2.urlopen(req).read()
            soup = BeautifulSoup(html,'html.parser')
            video_content=soup.find_all('div',class_=re.compile('j-video-c'))
            video_url=soup.find_all('div',class_=re.compile('^j-video$'))
            print(len(video_content))
            dic={}
            le=len(video_content)
            if le!=0:
                for i in video_url:
                    dic['video_url']=str(i['data-mp4']).strip()
                    dic['image_url']=str(i['data-poster']).strip()
                    dic['video_id']=str(i['data-id']).strip()
                    dic['title']=" "
                    dic['ti'] = " "
                    dic['public_date'] = " "
                    dbinfo=mysql_s.insertData("budejie",dic)
                    print(dbinfo)
                dic={}
                for i in video_content:
                    dic['video_id']=str(i['data-id']).strip()
                    dic['public_date']=str(i['data-date']).strip()
                    dic['title'] = str(i['data-title']).strip()
                    print(dic['title'])
                    dic['ti'] = str(i['data-time']).strip()
                    dbinfo=mysql_s.upData("budejie",dic)
                    print(dbinfo)
        except Exception as e:
            print("No Web Pages")

get_video_url_range(1,70)
