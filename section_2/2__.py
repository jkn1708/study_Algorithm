import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\section_2\input.txt","rt")

T=int(input())
for t in range(T):
    n,s,e,k=map(int,input().split())
    a=list(map(int,input().split()))
    answer=a[s-1:e]
    answer.sort()
    print(answer[k-1])

