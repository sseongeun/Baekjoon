def solution(sizes):
    list1=[]
    list2=[]
    for size in sizes:
        size.sort()
        list1.append(size[0])
        list2.append(size[1])
        
    return max(list1)* max(list2)
    