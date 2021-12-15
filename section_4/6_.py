#씨름 선수(그리디)
import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_4\input.txt")

profile=[]

n=int(input())
for i in range(n):
    t, w = map(int, input().split())
    profile.append((t,w))
profile.sort(reverse=True)
ht=0
hw=0
cnt=0

for x, y in profile:
    if y>hw:
        hw=y
        cnt+=1
    
print(cnt)

