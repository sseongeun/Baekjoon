def solution(n, arr1, arr2):
    result=[]

    for i in range(n):
        answer=""
        temp1 = str(bin(arr1[i])[2:])
        temp2 = str(bin(arr2[i])[2:])

        if len(temp1)!=n:
            temp1="0"*(n-len(temp1))+temp1
        if len(temp2)!=n:
            temp2="0"*(n-len(temp2))+temp2



        for i in range(n):
            if temp1[i]=="1" or temp2[i]=="1":
                answer+="#"
            else:
                answer+=" "
        result.append(answer)

    return result