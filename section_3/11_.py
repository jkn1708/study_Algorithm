#격자판 회문수

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_3\input.txt")

def solution(a):
    cnt=0
    for i in range(7):
        for j in range(3):
            answer= a[i][j:j+5]
            Ranswer=list(reversed(answer))
            if answer == Ranswer:
                cnt+=1
            for k in range(2):
                if a[j+k][i] != a[j+5-k-1][i]:
                    break
            else:
                cnt+=1
    

    return cnt



a = [list(map(int, input().split()))for _ in range(7)]

print(solution(a))
