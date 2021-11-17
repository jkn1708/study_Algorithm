#람다함수
plus_two=lambda x: x+2  #함수를 변수처럼 씀
print(plus_two(1))

a=[1,2,3]
print(list(map(plus_two,a)))
print(list(map(lambda x: x+1, a)))

