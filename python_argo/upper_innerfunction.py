msg="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp=msg.upper()
print(tmp)
print(tmp.find('T'))  #첫번째 T의 인덱스 번호를 출력
print(tmp.count('T')) #T의 갯수
print(msg[:2]) #0~1번위치까지 출력
print(msg[3:5]) #3,4번 출력
print(len(msg))  #전체길이, 공백포함
for i in range(len(msg)):
    print(msg[i],end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for a in msg:
    if a.isupper():             #대문자만 출력
        print(a, end=' ')

for a in msg:
    if a.isalpha():          #알파벳만 출력, 공백제거
        print(a, end=' ')    

abc = 'AZ'
for x in abc:
    print(ord(x))   #아스키코드 출력

ab='65'
print(chr(ab))  #아스키 숫자에 맞는 알파벳 출력

