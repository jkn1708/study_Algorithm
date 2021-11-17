'''
변수입력과 연산자
a,b=input("숫자를 입력하세요 :").split()
a=int(a)
b=int(b)
print(a+b)
'''
#같은방법으로
a,b=map(int,input("숫자를 입력하세요 :").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)   #목만 구하기
print(a%b)    #나머지만 구하기
print(a**b)   #거듭제곱