#함수 만들기

def add(a,b):
    c=a+b
    print(c)

add(3,2)

def add1(a,b):
    c=a+b
    d=a-b
    return c,d  #함수는 여러개의 값을 리턴할 수 있슴

print(add1(5,6))

def isPrime(x):      #소수이면 True를 반환함
    for i in range(2,x):
        if x%i==0:
            return False
    return True

a=[12,13,7,9,19]

for x in a:        #a리스트를 확인하면서 소수를 출력하기
    if isPrime(x):
        print(x, end=' ')
