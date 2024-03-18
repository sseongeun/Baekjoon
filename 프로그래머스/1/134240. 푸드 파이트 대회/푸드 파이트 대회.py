def solution(food):
    solution=[]
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            solution.append(i)
            
    newsolution=solution[::-1]
    solution.append(0)
    solution+=newsolution
    
    s=''.join(map(str,solution))
    return s