def solution(s):
    cnt1=0
    cnt2=0
    result=0
    x=""

    for i in s:
        if cnt1 == cnt2:
            x=i
            cnt1+=1
            result+=1
        elif i == x:
            cnt1+=1
        else:
            cnt2+=1
    return result