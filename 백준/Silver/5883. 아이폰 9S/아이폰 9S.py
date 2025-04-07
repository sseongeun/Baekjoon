from copy import deepcopy
import sys
input= sys.stdin.readline

N=int(input())
people=[]
for _ in range(N):
    people.append(int(input()))
    
people_set=set(people)

answer=[]
for p in people_set:
    temp=[]
    for i in people:
        if i!=p:
            temp.append(i)
    curr=temp[0]
    cnt=0
    result=[]
    for t in temp:
        if curr==t:
            cnt+=1
        else:
            curr=t
            result.append(cnt)
            cnt=1
    result.append(cnt)
    answer.append(max(result))
    
print(max(answer))