#사과나무

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_3\input.txt")
answer=0
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
x=y=n//2
for i in range(n):
    for j in range(x, y+1):
        answer+=a[i][j]
    if i<n//2:
        x-=1
        y+=1
    else:
        x+=1
        y-=1


print(answer)