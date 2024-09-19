def solution(number, k):
    final=len(number)-k
    stack=[]


    for i in number:
        while k>0 and stack and stack[-1]<i:
            k-=1
            stack.pop()
        stack.append(i)

    if k!=0:
        stack = stack[:-k]
    
    number="".join(stack)

    return number