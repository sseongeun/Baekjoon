from collections import deque
def solution(arr):
    answer=[]
    answer.append(arr[0])
    arr=deque(arr)

    while arr:
        curr =arr.popleft()
        if curr != answer[-1]:
            answer.append(curr)
    return answer