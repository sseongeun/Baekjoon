def solution(s):
    answer=[]
    result=[]

    for i in s:
        answer.append(ord(i))   
    answer.sort(reverse=True)


    for i in answer:
        result.append(chr(i))

    return ''.join(result)