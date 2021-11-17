import random as r
a=[]
b=list()

a[1,2,3,4,5]
print(a)
print(a[0])

b=list(range(1,11))
print(b)

c=a+b
print(c)

a.append(6)  #제일뒤에 추가
a.insert(3, 7) #특정 위치에 값을 대입(3번인덱스에 7이 대입됨)
print(a)
a.pop()  #제일 뒤에 인덱스 삭제
print(a)
a.pop(3)  #3번 인덱스의 값이 삭제
print(a)
a.remove(4)    #특정값을 찾아서 삭제(리스트에 4를 삭제함)
print(a)
print(a.index(5))  #5라는 값의 인덱스번호를 출력
print(sum(a)) #리스트의 값 모두 더하기
print(max(a)) #인자값들 중에 최대값 찾기
print(min(a))

r.shuffle(a)  #리스트를 랜덤으로 섞음
print(a)
a.sort()  #오름차순 정렬
print(a)
a.sort(reverse=True) #내림차순 정렬
print(a)
a.clear() #리스트 안에 내용 제거
print(a)
