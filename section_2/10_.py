import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_2\input.txt","rt")
score=0
cnt=0
n=int(input())
arr=list(map(int, input().split()))
for i in arr:
    if i==1:
        cnt+=1
        score+=cnt
    else:
        cnt=0
print(score)

    