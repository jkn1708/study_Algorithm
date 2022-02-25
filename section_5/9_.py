#아나그램

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_5\input.txt")

a=input()
b=input()
c=dict()
def solution(a,b):
    x=list(a)
    y=list(b)

    x.sort()
    y.sort()
    for i in range(len(x)):
        if len(x)!=len(y):
            answer='NO'
            break

        elif x[i]!=y[i]:
            answer='NO'

            break
        else:
            answer='YES'
    return print(answer)

solution(a,b)
