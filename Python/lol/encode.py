#from decimal to base

import string

d={}

def init(base):
    l=[str(x) for x in range(min(base,10))]
    l=''.join(l)
    if base>10:
        l+=string.ascii_uppercase[0:base-10]
    count=0
    for i in l:
        d[str(count)]=i;count+=1
    return d


def encode(n,base):
    l=[]
    x=n
    init(base)
    while(int(x)>0):
        l.append(str(int(x)%base))
        x=int(int(x)//base)
    l=l[len(l)::-1]
    l1=[d[y] if int(y)>9 else y for y in l]
    l1=''.join(l1)
    print(l1)

n=input()
base=30
encode(n,base)
