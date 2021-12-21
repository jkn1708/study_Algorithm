#침몰하는 타이타닉(그리디)

import sys
from collections import deque   # deque : 리스트에서 pop을 해도 앞뒤가 땡겨지지 않음

sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_4\input.txt")

n, m=map(int,input().split())
w=list(map(int,input().split()))
cnt=0
w.sort()
#w=deque(w)     리스트 deque로 변환

while w:                    # 리스트w의 내용이 없을때까지
    if len(w)==1:
        cnt+=1
        break
    if w[0]+w[-1]>m:
        w.pop()
        cnt+=1
    else:
        w.pop(0)            # w.popleft() 로 변환하면 같음
        w.pop()             
        cnt+=1                
print(cnt)

