import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_2\input.txt","rt")

def isPrime(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True
    

def reverse(x):
    res=0
    while x>0:
        a=x%10
        res=10*res+a
        x=x//10
    return res

n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    answer=reverse(i)
    if isPrime(answer):
        print(answer, end=" ")




