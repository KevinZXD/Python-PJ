#*-*coding:utf-8 *-*
'''
Created on 2016年9月17日

@author: 10678
'''
import pymysql
def testlist():
    list=[['zxd','asd','wer','frg'],['zxx','asd','wer','frg'],['zxc','asd','wer','frg']]
    for i in list:
        for j in i:
            print(j)
def conn():
    connection=pymysql.connect(host="localhost",user="root",passwd="kevin",db="python")
    try:
        cursor=connection.cursor()
        sql="insert into pydb(name,sex)valuse(%s,%s)"
        cursor.execute(sql,"zxx","male")
        connection.commit()
        print("成功！")
    except:
        print("出现异常")
    finally:
        connection.close()
    
if  __name__=="__main__":
    #conn()
    testlist()
    