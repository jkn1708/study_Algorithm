#후위표기식 계산

import sys
sys.stdin=open(r"C:\Users\Sang\Desktop\workspace\study\section_5\input.txt")
a=input()
ans=0
stack=[]

for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        if x=='+':
            ans= int(stack.pop()) + int(stack.pop())
            stack.append(ans)
        elif x=='-':
            ans= int(stack.pop())*-1 + int(stack.pop())
            stack.append(ans)
        elif x=='*':
            ans= int(stack.pop()) * int(stack.pop())
            stack.append(ans)
        elif x=='/':
            ans= int(stack.pop()) / int(stack.pop())
            stack.append(ans)
print(ans)






