#수들의 합
import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_3\input.txt")

n,m=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
p1=p2=0
for i in range(n):
    for j in range(i+1,n+1):
        

        if sum(arr[i:j])==m:
            cnt+=1
print(cnt)
