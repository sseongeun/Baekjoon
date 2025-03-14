from collections import deque

def solution(prices):
    answer=[]
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1,len(prices)):
            if prices[i]>prices[j]:
                cnt+=1
                break
            cnt+=1
        answer.append(cnt)

    return answer