def solution(n):
    result = 0

    for start in range(1,n+1):
        sum=0
        for i in range(start,n+1):
            sum+=i
            if sum == n:
                result+=1
                print("yes")
                break
            elif sum > n:
                break

    return result