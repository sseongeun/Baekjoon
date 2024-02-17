grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F':0.0
}


total=0
subNum=0
for i in range(20):
    new=list(map(str,input().split()))
    if(new[2]=="P"):
        continue
    else:
        new[1]=float(new[1])
        hj=grades[new[2]]
        total=total+new[1]*hj
        subNum=subNum+new[1]
    
print('%.6f' %(total/subNum))