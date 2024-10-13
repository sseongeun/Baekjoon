def solution(n, words):
    result=[0,0]
    voca=[]
    voca.append(words[0])
    
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            result[0]=(i%n+1)
            result[1]=(i//n+1)
            break
        elif words[i] in voca:
            result[0]=(i%n+1)
            result[1]=(i//n+1)
            break
        else:
            voca.append(words[i])
    return result