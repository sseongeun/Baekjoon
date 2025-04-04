voca=input()
result=""
flag=False
stack=[]

for char in voca:
    if char == "<":
        # 단어를 뒤집에서 넣는다
        while stack:
            result+= stack.pop()
        flag=True
        result+=char
    elif char == ">":
        flag=False
        result+=char
    elif flag:
        result+=char
    elif char == " ":
        while stack:
            result+= stack.pop()
        result+=char
    else:
        stack.append(char)
        
while stack:
    result+=stack.pop()
    
print(result)