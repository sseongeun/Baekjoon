answer =0 

def dfs(numbers,target,index,curr):
    
    global answer
    
    if index == len(numbers) and curr== target:
        answer+=1
        return
    
    elif index == len(numbers):
        return
    
    dfs(numbers,target,index+1,curr-numbers[index])
    dfs(numbers,target,index+1,curr+numbers[index])


def solution(numbers, target):
    
    global answer 
    
    dfs(numbers,target,0,0)

    return answer


