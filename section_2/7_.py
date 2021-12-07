#소수(에라토스테네스 체) 

import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_2\input.txt","rt")
n=int(input())
ch=[0]*(n+1)
cnt=0
answer=[]
for i in range(2,n+1):
    if ch[i]==0:
        answer.append(i)
        for j in range(i,n+1,i):
            ch[j]=1
print(answer)