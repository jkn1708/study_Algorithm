import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_2\input.txt","rt")

n=int(input())
answer=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    tmp.sort()
    if tmp[0] == tmp[1] and tmp[1] ==tmp[2]:
        money= 10000+(tmp[0]*1000)
    elif tmp[0] == tmp[1]:
        money= 1000+(tmp[0]*100)
    elif tmp[1] == tmp[0]:
        money= 1000+(tmp[1]*100)
    else:
        money=tmp[0]*100
    answer.append(money)
print(max(answer))
