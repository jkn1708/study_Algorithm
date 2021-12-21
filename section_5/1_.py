#가장 큰수

import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_5\input.txt")


num, m= map(int, input().split())
cnt=0
arr=[]
stack=[]
for i in str(num):
    arr.append(int(i))
    
for x in arr:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str,stack))
print(res)

        
    

        
