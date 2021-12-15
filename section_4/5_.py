#회의실 배정(그리드)

import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_4\input.txt")

n= int(input())
meeting=[]
for i in range(n):
    s, e =map(int,input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x : (x[1],x[0]))
et=0
cnt=0
for s,e in meeting:

    if s>=et:
        et=e
        cnt+=1
print(cnt)