import math

from urllib3.connectionpool import xrange

def blabla():
    liste = []
    for i in xrange(10):
        liste.append(i)

    print(liste)

def Binary_Search(A,v):
    n = math.floor(len(A)/ 2)
    print(A[n],n)
    while(n <= 0):

        if(A[n]==v):
            print(n)
            break
        if(A[n]<v):
            temp = []
            for i in xrange(0,n+1):
                temp.append(A[i])
            A = temp
            print(temp)
            n = math.floor(n/2)
        if(A[n]>v):
            index = 0
            temp2 = []

            for i in xrange(n,len(A)+1):
                temp2.append(A[i])
                index += 1

            print(temp2)
            A = temp2
            n = math.floor(n/2)

    print("Nicht Gefunden")
    return n


B =[1,2,3,4,5]
v=2
Binary_Search(B,v)


