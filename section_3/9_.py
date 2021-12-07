#봉우리

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_3\input.txt")
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
cnt=0
for x in a:
    x.insert(0, 0)
    x.append(0)

for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
            cnt+=1
print(cnt)
