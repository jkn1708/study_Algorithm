#응급실
import sys
sys.stdin=open(r"C:\Users\sanghyeon\Desktop\VS_workspace\section_5\input.txt")
n, m = map(int,input().split())
arr=[(pos,val) for pos,val in enumerate(list(map(int,input().split())))]   #[(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)] 이런식으로 위치값과 밸류값을 가지는 배열로 구현

#위에랑 같은 얘기 풀어쓴거
# arr=list(map(int,input().split()))
# arr1 =[]
# for pos,val in enumerate(arr):
#     arr1.append((pos,val))

def solution(n,m,arr):
    cnt=0
    while True:
        cur=arr.pop(-1)
        if any(cur[1]<x[1] for x in arr):    #any는 any()안의 값이 하나라도 참이 면 참으로 인정
            arr.append(cur)
        else:
            cnt+=1
            if cur[0]==m:
                return cnt

print(solution(n,m,arr))




#만약 차근차근 앞에서 부터 샌다면
# arr=list(map(int,input().split()))

# def solution(n,m,arr):
#     cnt=1

#     while(len(arr)>0):
#         for i in range(n):
#             if arr[i] == max(arr):
#                 arr.pop(-1)
#                 if m==0:
#                     return cnt
            
#             else:
#                 arr.append(arr[i])
#                 arr.pop(-1)
#                 if m==0:
#                     m=m+len(arr)+1
#             m-=1
#             cnt+=1

# print(solution(n,m,arr))







