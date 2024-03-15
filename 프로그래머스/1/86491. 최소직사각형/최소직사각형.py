def solution(sizes):
    garo=[]
    sero=[]

    for i in sizes:
        i.sort(reverse=True)
        garo.append(i[0])
        sero.append(i[1])
    
    return max(garo)*max(sero)