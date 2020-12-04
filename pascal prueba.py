# -*- coding: utf-8 -*-
x=int(input('digita un número '))
i=x
i2=0
n=0 
k=0 
import math 
while (n<=x):  
    print( ' ' ) 
    print( ' ' ) 
    print( ' ' ) 
    while(k<=n): 
        c=n-k 
        p=math.factorial(c) 
        s=math.factorial(k) 
        n1=math.factorial(n) 
        k1=p*s 
        rta=n1/k1 
        k=k+1
        listrta=[]
        listrta[len(listrta):]=[rta]
        while(i>=0):
            j=[]
            j[len(j):] = [i]
            i=i-1
            print (str(listrta)+"x^"+str(j))
            print(end="")
        while(i2<=x):
            f=[]
            f[len(f):] = [i2]
            i2=i2+1
            print(str(listrta)+"y^"+str(f))
            print(end="")
    n=n+1 
    k=0