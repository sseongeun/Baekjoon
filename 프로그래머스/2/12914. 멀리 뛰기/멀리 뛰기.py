def solution(n):
    a=1;b=1
    answer=1
    for i in range(n-1):
        answer=a+b
        a=b
        b=answer

    return answer%1234567