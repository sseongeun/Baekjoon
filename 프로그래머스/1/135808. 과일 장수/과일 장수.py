def solution(k, m, score):
    sum=0
    score.sort()
    box=len(score)//m #박스의 개수
    for i in range(box):
        for j in range(m):
            num=score.pop()
        sum+=num*m
    return sum
    