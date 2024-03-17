def solution(numbers):
    sum=[]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            sum.append(numbers[i]+numbers[j])
    sum=list(set(sum))
    sum.sort()
    return sum