def solution(k, score):
        L=[]
        result=[]


        for i in score:
            L.append(i)
            if(len(L)>k):
                L.remove(min(L))
                L.sort(reverse=True)
            result.append(min(L))
        
        return result