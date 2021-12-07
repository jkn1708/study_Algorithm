#k번째 큰 수
import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\section_2\input.txt","rt")

n,k = map(int,input().split())
a=list(map(int,input().split()))
res=set()       # 중복이 없는 형태의 리스트
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            res.add(a[i]+a[j]+a[l])
res=list(res)
res.sort(reverse=True)
print(res[k-1])

