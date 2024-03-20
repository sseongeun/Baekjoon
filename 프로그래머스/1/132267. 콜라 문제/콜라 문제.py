def solution(a, b, n):
    sum=0
    rem=0

    while(n>=a):
        rem=n%a
        n=n//a*b
        sum+=n
        n+=rem
    
    return sum