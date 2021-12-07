#회문 문자열 검사
import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_3\input.txt","rt")

n=int(input())
for i in range(n):
    tmp=input()
    tmp=tmp.upper()
    size=len(tmp)
    for j in range(size//2):
        if tmp[j]!=tmp[-1-j]:  #tmp[::-1]  -> 문자열 거꾸로 만드는 법
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))


        
        
