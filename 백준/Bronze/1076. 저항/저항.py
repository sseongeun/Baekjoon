color_dict = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "grey": (8, 100000000),
    "white": (9, 1000000000)
}

answer=[]
for i in range(3):
    answer.append(input())
    
num=color_dict[answer[0]][0]*10+color_dict[answer[1]][0]

print (num*color_dict[answer[2]][1])