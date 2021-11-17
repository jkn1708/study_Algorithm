#1차원 리스트
a=[0]*3
print(a)

#2차원 리스트
b=[[0]*3 for _ in range(3)]
print(b)

b[0][1]=1
print(b)

for x in b:
    print(x)

for x in b:     #2차원 리스트를 행렬의 형태로
    for y in x:
        print(y, end=" ")   
    print()    #행마다 줄바꿈
