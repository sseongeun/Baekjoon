def solution(n, lost, reserve):
    lost_set=set(lost)-set(reserve)
    reserve_set=set(reserve)-set(lost)


    for i in lost_set:
        if (i-1) in reserve_set:
            reserve_set.remove(i-1)
        elif (i+1) in reserve_set:
            reserve_set.remove(i+1)
        else:
             n-=1

    return n