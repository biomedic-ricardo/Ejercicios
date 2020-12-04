# Ricardo & Carlos
# put a int type number which is saved in x 
x=int(input('put a number '))
#n and k must be in 0 to do the "while" corretly
n=0 
k=0 
import math 
# do a loop from 0 to x
while (n<=x): 
    #put 3 spaces to separate the coeficient levels
    print( ' ' ) 
    print( ' ' ) 
    print( ' ' )
    # do a loop from 0 to n
    while(k<=n):
        #we made a substraction between n and k and put it in c 
        c=n-k 
        #do a factorial of c and put it in p
        p=math.factorial(c)
        #do a factorial of k and put it in p
        s=math.factorial(k) 
        #do a factorial of n and put it in n1
        n1=math.factorial(n)
        #do a multiplication of p and s to put it in k1
        k1=p*s 
        #this is the pasacal equation simplificated with the
        #before information
        rta=n1/k1 
        #star the count to finish the loop
        k=k+1 
        #show the pascal triagule with string data
        print(str(rta)+"x^"+str(c)+"+y^"+str(k-1),end="  ")    
    #also star the count in n to finish the loop
    n=n+1 
    k=0 