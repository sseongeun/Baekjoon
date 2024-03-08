def solution(name, yearning, photo):
    answer = []
    dic=dict(zip(name,yearning))
    
    for i in range(len(photo)):
        sum=0
        for j in range(len(photo[i])):
             if photo[i][j] in name:
                sum+=dic[photo[i][j]]
        answer.append(sum)
    
    return answer