#역수열(그리디)
import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_4\input.txt")

n= int(input())
arr=list(map(int,input().split()))
seq=[0]*n

for i in range(n):
    for j in range(n):
        if arr[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            arr[i]-=1

print(seq)

