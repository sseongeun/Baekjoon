def solution(sizes):
    garo=[]
    sero=[]

    for i in sizes:
        i.sort(reverse=True)
        garo.append(i[0])
        sero.append(i[1])

    g=max(garo)
    s=max(sero)

    return g*s