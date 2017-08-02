#-*- coding:utf-8 -*-
import urllib2
import re
import csv
from bs4 import BeautifulSoup

'''
get_volumn_url_set()获取一级url
仍需要get_abstract_url_set_volumn（volumn）继续获取url的内容并把摘要的url提取出来组成abstract_url
volumn_url:url_start

目标url类似这种：http://www.eope.net/CN/abstract/abstract16318.shtml
'''
volumn_set=[]
abstract_set=[]
all_person=[]
url_start=u"http://www.eope.net/CN/volumn/home.shtml"
def get_abstract_url_set_start(url_start):
    html=urllib2.urlopen(url_start)
    html_content=str(html.read())
    soup=BeautifulSoup(html_content,'html.parser')
    url_set=soup.find_all('a',href=re.compile("../abstract/abstract"))
    print(len(url_set))
    for url_sub in url_set:
        url_string=url_sub['href']
        abstract_url=u"http://www.eope.net/CN"+url_string[2:]
        abstract_set.append(abstract_url)
        print(abstract_url)
def get_abstract_url_set_volumn(volumn_url):
    html=urllib2.urlopen(url_start)
    html_content=html.read()
    soup=BeautifulSoup(html_content,'html.parser')
    url_set=soup.find_all('a',href=re.compile("../abstract/abstract"))
    print(len(url_set))
    for url_sub in url_set:
        url_string=url_sub['href']
        abstract_url=u"http://www.eope.net/CN"+url_string[2:]
        abstract_set.append(abstract_url)
        print(abstract_url)
def get_volumn_url_set():
    url=u"http://www.eope.net/CN/article/showOldVolumn.do"
    html=urllib2.urlopen(url)
    html_conte=html.read()
    html_content=html_conte
    soup=BeautifulSoup(html_content,'html.parser')
    url_set=soup.find_all("a",class_=re.compile("J_WenZhang"))
    print(len(url_set))
    i=0
    for url_sub in url_set:
        url_string=url_sub['href']
        volumn_url=u"http://www.eope.net/CN"+url_string[2:]
        print(volumn_url)
        volumn_set.append(volumn_url)
        i+=1
        if i<20:
            get_abstract_url_set_volumn(volumn_url)
def write2csv(file_url):
    #all_person列表 记录所有作者信息（以列表方式储存） 理想的最终版本 写作者信息进入csv 
    wf=open(file_url,'wb')
    writer=csv.writer(wf)
    writer.writerow((' id ',' url ',' email ',' name ',' sex ',' birth ',' unit ','address','degree','tutor','job'))
    #person_set=set(all_person)
    #all_person=list(person_set)
    i=0
    import sys
    reload (sys)
    sys.setdefaultencoding('utf-8')
    for person_info in all_person:
        i+=1
        writer.writerow((i,person_info['url'],person_info['email'].encode("gbk"),person_info['name'].encode("gbk"),person_info['sex'].encode("gbk"),person_info['birth'].encode("gbk"),person_info['unit'].encode("gbk"),person_info['address'].encode("gbk"),person_info['degree'].encode("gbk"),person_info['tutor'].encode("gbk"),person_info['job'].encode("gbk")))
    wf.flush()
    wf.close()
def parse_author_info(abstract_url):
    person=[]
    person_info={}
    html=urllib2.urlopen(abstract_url)
    abstract_url_content=html.read()
    soup=BeautifulSoup(abstract_url_content,'html.parser')
    author_content=soup.find_all("span",class_=re.compile("J_zhaiyao"))
    unit_text=soup.find_all('td',style=re.compile("line-height:130%"))
    unit=unit_text[0].get_text().split(";")[0]
    index=len(author_content)-1
    if index>0:
        text=author_content[index].get_text().split()
        person.append(text[1].encode("utf-8"))
        solit=person[0].decode("utf-8").split(',')   
        if(person[0].find("E-mail")):
            index=person[0].index("E-mail")
            email=person[0][index+7:]
            index_name=person[0].index("(")
            name=person[0][0:index_name].decode("utf-8")
            birth=person[0][index_name+1:index_name+5]
            index_p=person[0].index("人")
            
            sex_index=person[0].find("男")
            if sex_index:
                sex=u"男"
            else:
                sex_index=person[0].find("女")
                sex=u"女"
            address=solit[2]
            degree_boshi=person[0].find("博士")
            if degree_boshi:
                degree=u"博士"
            else:
                if person[0].find("硕士"):
                    degree=u"硕士"
                else:
                    if person[0].find("本科"):
                        degree=u"本科"
                    else:
                        degree=u"本科以下"
            tutor_index=person[0].find("导师")
            if tutor_index<0:
                tutor=person[0][tutor_index-9:tutor_index+6].decode("utf-8")
            else:
                tutor=u"没有信息"
            job_index=person[0].find("主要从事")
            job=person[0][job_index:index].decode("utf-8")
            person_info['name']=name
            person_info['birth']=birth
            person_info['sex']=sex
            person_info['address']=address
            person_info['degree']=degree
            person_info['tutor']=tutor
            person_info['job']=job
            person_info['email']=email
            person_info['unit']=unit[2:]
            person_info['url']=abstract_url
            for i in person_info:
                print(i+":"+person_info[i])
            all_person.append(person_info)
            #print("all_person加入"+name)
def spaser():
    print("Sparsing is start")
    file_url=u"D:person_info.csv"
    get_abstract_url_set_start(url_start)
    get_volumn_url_set()
    for abstract_url in abstract_set:
        parse_author_info(abstract_url)
    print(type(all_person[0]))
    write2csv(file_url)
    print("Sparsing is over")
        
#text=get_abstract_url_author_content(u'http://www.eope.net/CN/abstract/abstract16318.shtml')
#get_abstract_url_set_start(url_start)
#get_volumn_url_set()
spaser()
																																


