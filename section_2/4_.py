import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_2\input.txt","rt")

n=int(input())
a=list(map(int,input().split()))
ave=round(sum(a)/n)    #round : 반올림
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-ave)            #abs : 절대값
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(ave, res)


