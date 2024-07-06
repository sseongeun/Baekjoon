def solution(money):
    answer = []
    num=money//5500
    answer.append(num)
    answer.append(money-5500*num)
    
    return answer