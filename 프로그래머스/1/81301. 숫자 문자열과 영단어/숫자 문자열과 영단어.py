from collections import deque

def solution(s):
    match={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    num=['0','1','2','3','4','5','6','7','8','9']
    key_list=match.keys()

    s=deque(list(s))

    l=[]
    voca=""
    curr=""

    while s:
        curr+=s.popleft()
        if curr in num:
            voca+=curr
            curr=""
        else:
            if curr in key_list:
                voca+=str(match[curr])
                curr=""
    return int(voca)
        
    