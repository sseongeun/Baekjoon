def solution(a, b):
    week={4:"MON",5:"TUE",6:"WED",0:"THU",1:"FRI",2:"SAT",3:"SUN"}

    days=[31,29,31,30,31,30,31,31,30,31,30,31]


    total=0
    for i in range(a-1):
        total+=days[i]
    total+=b

    return str(week[total%7])