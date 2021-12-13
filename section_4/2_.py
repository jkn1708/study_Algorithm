#랜선자르기(결정알고리즘)
import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\input.txt")
sum=0
a=[]
sum1=[]
k=list(map(int,input().split()))
for i in range(k[0]):
    cm=int(input())
    a.append(cm)
    sum+=cm
answer=sum//k[1]
for i in range(k[0]):
    for j in range(answer,0,-1):
        sum1+=i

    