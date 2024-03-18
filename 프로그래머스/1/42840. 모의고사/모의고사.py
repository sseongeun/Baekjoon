def solution(answers):
    s1=[1,2,3,4,5]*2000
    s2=[2,1,2,3,2,4,2,5]*1250
    s3=[3,3,1,1,2,2,4,4,5,5]*1000
    L1,L2,L3=[],[],[]

    for i in range(len(answers)):
        L1.append(answers[i]-s1[i])
        L2.append(answers[i]-s2[i])
        L3.append(answers[i]-s3[i])


    L=[L1.count(0),L2.count(0),L3.count(0)]
    maxNum=max(L)

    solution=[]

    for i in range(3):
        if maxNum==L[i]:
            solution.append(i+1)


    return solution