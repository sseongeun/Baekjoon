def check_string(s):
    stack=[]
    for i in s:
        if i == '[' or i=='{' or i =='(':
            stack.append(i)
        else:
            if i==']':
                if stack and stack[-1]=='[': stack.pop() 
                else : stack.append(i)
            elif i=='}':
                if stack and stack[-1]=='{': stack.pop() 
                else : stack.append(i)
            else:
                if stack and stack[-1]=='(': stack.pop() 
                else : stack.append(i)
                
    if len(stack)==0 :return 1
    else: return 0

def solution(s):
    s=list(s)
    s_len=len(s)
    s=s*2
    answer=0
    for i in range(s_len):
        temp =s[i:i+s_len]
        answer+=check_string(temp)

    return answer