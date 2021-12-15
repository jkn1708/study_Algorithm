#마구간 정하기 (결정알고리즘)

import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_4\input.txt")

n,c = map(int,input().split())
a=[int(input()) for _ in range(n)]
a.sort()
lt=1
rt=a[n-1]
res=0
def Count(len):
    cnt=1
    ep=a[0]
    for i in range(1,n):
        if a[i]-ep>=len:
            cnt+=1
            ep=a[i]
    return cnt




while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

