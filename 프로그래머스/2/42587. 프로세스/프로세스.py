from collections import deque

def solution(priorities, location):
    priorities=deque(priorities)
    answer=0
    while location != -1:
        curr=priorities.popleft()

        if len(priorities)==0:
            answer+=1
            break

        if curr >= max(priorities): # 뽑아야 하는 경우
            answer+=1
            location-=1

            if location == -1:

                break
        else:
            priorities.append(curr)
            if location ==0:
                location=len(priorities)-1
            else:
                location-=1

    return answer