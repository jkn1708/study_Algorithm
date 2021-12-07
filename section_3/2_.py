#숫자만 추출

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_3\input.txt","rt")
res=0
cnt=0
a=input()
for i in a:
    if i.isdigit():
        res=res*10+int(i)
print(res)

for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)


