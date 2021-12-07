#카드 역배치

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_3\input.txt","rt")
card=list(range(1,21))

for _ in range(10):
    ai, bi=map(int,input().split())
    new_card=list(reversed(card[ai-1:bi]))
    card[ai-1:bi]=new_card

print(' '.join(list(map(str,card))))

    

