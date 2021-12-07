'''
조건문


x=7
if x>0 and x<10:
    print("10보다 작은 자연수")
'''
#continue : 바로 다음 순번의 loop를 수행
#break : 반복문을 멈추고 loop 밖으로 나감
'''
반복문


for i in range(10,0,-1):
    print(i)

i=1
while i<=10:
    print(i)
    i=i+1 #i+=1

while True:
    print(i)
    if i==10:
        break
    i+=1

for i in range(1,11):
    if i%2==0:
        continue
    print(i)

for i in range(1,11):
    print(i)
    if i==5:
        break
else:
    print(11)

'''

'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수출력하기

#1번
n=int(input())
for i in range(1,n+1):
    if i%2==1:
        print(i)

#2번
sum = 0
n=int(input())
for i in range(1,n+1):
    sum=sum+i
print(sum)
'''
#3번
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ')

