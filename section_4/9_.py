#증가수열 만들기 (그리디)

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_4\input.txt")

n=int(input())
m=list(map(int, input().split()))
a=''
b=[]
if m[0] < m[-1]:
    a='L'
    b.append(m[0])
    m.pop(0)
else:
    a='R'
    b.append(m[-1])
    m.pop()

while m:
    if len(m)==1 and m[0]>b[-1]:
        a+='L'
        b.append(m[0])
        m.pop()
    elif m[0] > b[-1] >m[-1]:
        a+='L'
        b.append(m[0])
        m.pop(0)
        
    elif m[-1] > b[-1] > m[0]:
        a+='R'
        b.append(m[-1])
        m.pop()
    elif m[-1]>m[0]>b[-1]:
        a+='L'
        b.append(m[0])
        m.pop(0)
    elif m[0]>m[-1]>b[-1]:
        a+='R'
        b.append(m[-1])
        m.pop()
    else:
        break

print(len(a))
print(a)
