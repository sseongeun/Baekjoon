def solution(s):
    key_list=['[',']','{','}','(',')']
    value_list=[1,-1,2,-2,3,-3]
    dic=dict(zip(key_list,value_list))

    turn =len(s)
    s = s*2 
    
    result=0
    for start in range(turn):
        stack = []
        prev=0
        for i in range(start,start+turn):

            if prev == -dic[s[i]]  and prev>dic[s[i]]:
                stack.pop()
            else:
                stack.append(dic[s[i]])
                prev= dic[s[i]]


            if stack: 
                prev=stack[-1]
            else:
                prev =0
        if len(stack)==0:
            result+=1
    
    return result