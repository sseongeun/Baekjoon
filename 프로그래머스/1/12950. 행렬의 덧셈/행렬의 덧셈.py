def solution(arr1, arr2):
    answer=[]

    for i in range(len(arr1)):
        L=[]
        for j in range(len(arr1[0])):
            L.append(arr1[i][j]+arr2[i][j])
        answer.append(list(L))


    return answer
