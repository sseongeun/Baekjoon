def solution(s):
    numof0= 0
    cnt=0
    result=[]


    while (s!="1"):
        cnt+=1
        numof0 += s.count("0")
        numof1 = s.count("1")
        s=bin(numof1)[2:]

    result.append(cnt)
    result.append(numof0)
    return result