import pymysql
def conn():
    con= pymysql.connect(host='localhost',user='root',password='kevin',db='python')
    cursor =con.cursor()
    sql ="select * from pydb"
    sql1="insert into pydb(name,sex)values(%s,%s)"
    #����������list���ݽṹ
    cursor.execute(sql1,["zx","le"])
    cursor.execute(sql)
    row=cursor.fetchone()
    print( row)
    cursor.close()
    con.commit()
    con.close()
conn()