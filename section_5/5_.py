#공주구하기(큐 자료구조로 해결)

import sys
from collections import deque
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_5\input.txt")
n, k = map(int,input().split())
cnt=0
n1=0
prin=[]
for x in range(1,n+1):
    prin.append(x)

prin=deque(prin)

while True:
    cnt+=1
    if len(prin)==1:
        break
    elif cnt==k:
        prin.popleft()
        cnt=0
    else:
        n1=prin[0]
        prin.popleft()
        prin.append(n1)

print(prin[0])

            