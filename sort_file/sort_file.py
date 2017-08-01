#-*- coding:utf-8 -*-

def read_from_chinease(path):
    with open(path) as f:
        for line in f:
            yield line

def sortfile(p):
    try:
        words=" "
        while True:
            if "赵" in words:
                print(words)
                with open("E:/text/"+words[0:2]+'.txt','w') as f:
                    while True:
                        words=p.__next__()
                        if "赵" in words:
                            break
                        f.write(words)
            else:
                words=p.__next__()
    except Exception as e:
        print("文件处理完毕")
        print(e)
if __name__=="__main__":
    p=read_from_chinease("E:/text/zxd.txt")
   # print(p.next())
    #f=open("E:/text/zxd.txt")
    sortfile(p)
    #print(f.readlines())