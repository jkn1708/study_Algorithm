#곳감(모래시계)

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_3\input.txt")
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
m=int(input())

x=0
y=n-1
answer=0

for i in range(m):
    h,t,k=map(int,input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())


for i in range(n):
    for j in range(x,y+1):
        answer+=a[i][j]
    if i<n//2:
        x+=1
        y-=1
    else:
        x-=1
        y+=1

print(answer)

