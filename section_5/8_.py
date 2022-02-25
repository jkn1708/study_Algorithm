#단어 찾기

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_5\input.txt")

n=int(input())
n1=n-1
word=[]
write=[]
#리스트형태로
for i in range(n):
    a=input()
    word.append(a)
for i in range(n1):
    b=input()
    write.append(b)

def solution(word,write):
    set1=set(word)
    set2=set(write)
    set3=set1-set2
    answer=list(set3)

    return answer[0]

print(solution(word,write))



