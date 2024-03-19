def solution(array, commands):
    array=[0]+array
    answer=[]

    for i in commands:
        newArray=array[i[0]:i[1]+1]
        newArray.sort()
        answer.append(newArray[i[2]-1])
    return answer
    