a=[1,2,3,4,5]
for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x,end=' ')
print()

for x in enumerate(a):   #인덱스번호와 그 값을 같이 출력해줌
    print(x)

b=(3,4,5,6) #튜플(안의 내용을 수정할 수 없음)
# b[0]=7 이거는 불가능

for x in enumerate(a):   
    print(x[0],x[1])    #인덱스 번호와 값을 따로따로 출력할 수 있음
print()

for index, value in enumerate(a):
    print(index,value)    #위와 똑같이 인덱스 번호와 값을 따로따로 출력할 수 있음
print()

if all(5>x for x in a):   #all은 안의 내용이 모두 참이여야 참임
    print("YES")
else:
    print("NO")

if any(5>x for x in a):   #any은 안의 내용들 중 하나라도 참이면 참임
    print("YES")
else:
    print("NO")
