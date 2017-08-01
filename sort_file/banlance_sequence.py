def mean(sorted_list):
    if not sorted_list:
        return (([],[]))
    big = sorted_list[-1]
    small = sorted_list[-2]
    big_list, small_list = mean(sorted_list[:-2])
    big_list.append(small)
    small_list.append(big)
    max1 = sum(big_list)
    min1 = sum(small_list)
    if (max1 > min1):
        return ((big_list, small_list))
    else:
        return ((small_list, big_list))

#unsupported operand type(s) for +: 'int' and 'list'  不知道如何解决
def mime(l,r):
    lis=[]
    for i in r:
        l.append(i)
    lis=l
    lis.sort()
    print(lis)
    l=[]
    r=[]
    i=0
    while i+1<=len(lis)-1:
        if(sum(l)>=sum(r)):
            l.append(lis[i])
            r.append(lis[i+1])
            i+=2
        else:
            r.append(lis[i])
            l.append(lis[i+1])
            i+=2

    print(l)
    print(r)
'''s = [[12, 33, 44, 66,],[7777, 4444, 123, 555]]
mime(s[0],s[1])
s1=[1,4,66,77,88,99,12,34]
s1.sort()
big,small=mean(s1)
print(s1)
print(big)
print(small)'''

def minsumvalue():
    a=[-1,-2,0,2,4,-7,8,9,10,-12,10,3,2]
    thissum=0
    maxsum=-1024
    for i in range(len(a)):
        thissum+=a[i]
        if(thissum>maxsum):
            maxsum=thissum
        if(thissum<0):
            thissum=0
    print(maxsum)
minsumvalue()

