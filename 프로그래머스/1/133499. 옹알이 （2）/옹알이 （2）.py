def solution(babbling):
    result=0
    for i in babbling:
        prev=""
        while len(i)!=0:
            if len(i)>=3 and i[:3]=="aya" and prev!="a":
                i=i[3:]
                prev="a"
            elif  len(i)>=3 and i[:3]=="woo" and prev!="w":
                i=i[3:]
                prev="w"
            elif len(i)>=2 and i[:2]=="ye" and  prev!="y":
                i=i[2:]
                prev="y"
            elif len(i)>=2 and i[:2]=="ma" and  prev!="m" :
                i=i[2:]
                prev="m"
            else:
                break
        if len(i)==0:
            result+=1

    return result