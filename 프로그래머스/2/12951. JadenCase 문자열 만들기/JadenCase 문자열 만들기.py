def solution(s):
    
    S=s.split(" ")
    answer=[]
    for i in range(len(S)):
        S[i]=S[i].capitalize()


    answer=" ".join(S)
    return answer