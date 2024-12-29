from collections import deque

def func(commands):
    dq = deque()
    result = []
    for command in commands:
        if "push_front" in command:
            dq.appendleft(int(command.split()[1]))
        elif "push_back" in command:
            dq.append(int(command.split()[1]))
        elif command == "pop_front":
            result.append(dq.popleft() if dq else -1)
        elif command == "pop_back":
            result.append(dq.pop() if dq else -1)
        elif command == "front":
            result.append(dq[0] if dq else -1)
        elif command == "back":
            result.append(dq[-1] if dq else -1)
        elif command == "size":
            result.append(len(dq))
        elif command == "empty":
            result.append(1 if not dq else 0)

    return result
       
    
n =int(input())
commands=[]
for i in range(n):
    commands.append(input())

answer=func(commands)
for i in answer:
    print(i)