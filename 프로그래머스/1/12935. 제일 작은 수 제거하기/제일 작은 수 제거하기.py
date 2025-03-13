def solution(arr):
    minNum= min(arr)
    arr.remove(minNum)

    if len(arr)==0:
        return [-1]
    else:
        return arr
    