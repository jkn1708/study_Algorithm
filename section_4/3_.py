#뮤직비디오(결정알고리즘)

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_4\input.txt")


n, m = map(int, input().split())
song=list(map(int, input().split()))
res=0
sum1=sum(song)
lt=1
rt=sum1

def Count(capacity):
    cnt=1
    sum=0
    for x in song:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt


while lt<rt:
    mid=(lt+rt)//2
    if Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1

print(res)
        

