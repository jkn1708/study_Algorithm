#창고 정리

import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_4\input.txt")

L= int(input())
box = list(map(int, input().split()))
m= int(input())

ma=0
mi=0

for i in range(m):
    box[box.index(max(box))]= box[box.index(max(box))]- 1
    box[box.index(min(box))]= box[box.index(min(box))]+ 1

print(max(box)-min(box))


# 다른방법은 sort를 통해 맨 앞자리나 뒷자리로 최대값 최소값 추출