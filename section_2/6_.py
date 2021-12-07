#자리수의 합

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_2\input.txt","rt")
n=int(input())
num=list(map(int,input().split()))
'''
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
        return sum
max=0
for x in num:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(x)
'''
#편한 방법
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
        return sum
max=0
for x in num:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(x)