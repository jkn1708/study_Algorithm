#두 리스트 합치기
import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_3\input.txt")
# arr=[]
# a1=int(input())
# b1=list(map(int, input().split()))
# for i in b1:
#     arr.append(i)

# a2=int(input())
# b2=list(map(int, input().split()))
# for j in b2:
#     arr.append(j)

# arr.sort()
# for i in arr:
#     print(i, end=" ")

# O(n)
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
else:
    c=c+b[p2:]
print(c)