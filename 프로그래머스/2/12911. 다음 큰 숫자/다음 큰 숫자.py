def solution(n):
    
    s=str(bin(n))
    print(s.lstrip("0b"))
    num1=s.count("1")


    while(True):
        n+=1
        s=str(bin(n))
        s.lstrip("0b")
        if(num1==s.count("1")):
            return n