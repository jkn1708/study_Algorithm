#이분 검색

import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\input.txt")

n=list(map(int, input().split()))
m=list(map(int, input().split()))
m.sort()
for i in range(n[0]):
    if m[i]==n[1]:
        print(i+1)




