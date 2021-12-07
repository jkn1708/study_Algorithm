#정다면체

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_2\input.txt","rt")
max=0
answer=[]
n,m=map(int,input().split())
cnt=[0]*(n+m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        answer.append(i)
print(answer, end=' ')


        