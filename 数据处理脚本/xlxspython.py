#-*- coding: utf8 -*-
import xlrd
from xlwt import Workbook
#from pyExcelerator import *
def readxlsx(fileaddress):
    f=open('E:zxd.txt','w')
    fname = fileaddress
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
     sh = bk.sheet_by_name("Sheet1")
    except:
     print ("no sheet in %s named Sheet1" % fname)
    #获取行数
    nrows = sh.nrows
    #获取列数
    ncols = sh.ncols
    print ("nrows %d, ncols %d" % (nrows,ncols))
    #获取第一行第一列数据 
    cell_value = sh.cell_value(1,1)
    #print (cell_value) 
    row_list = []
    #获取各行数据
    w =Workbook('E:mini.xls')  
    ws = w.add_sheet('2015 grade',cell_overwrite_ok=True)
    for i in range(0,nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)
        ws.write(i,0,row_data[0])
        ws.write(i,1,row_data[1])
        ws.write(i,2,row_data[2])
        ws.write(i,3,row_data[3])
        ws.write(i,4,row_data[4])
        ws.write(i,5,row_data[36])
        ws.write(i,6,row_data[40])
        if(i>0):
            ws.write(i,7,row_data[3]+row_data[4])
        else:
            ws.write(i,7,'第二学年的总学分')

    w.save('E:mini.xls')
def writeXlsx():
    w =Workbook('E:mini.xls')  #创建一个工作簿
    ws = w.add_sheet('Hey, Hades') #创建一个工作表
    ws.write(0,0,'bit')#在1行1列写入bit
    ws.write(0,1,'huang')#在1行2列写入huang
    ws.write(1,0,'xuan')#在2行1列写入xuan
    w.save('E:mini.xls')#保存
readxlsx('E:1.xls')
