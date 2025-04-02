N,M=map(int,input().split()) # 숫자 개수, 목표 합계
nums = list(map(int,input().split()))

cnt = 0
start =0
end =0 
curr_sum =0 

while True:
    if curr_sum>M:
        curr_sum-=nums[start]
        start+=1
        
    elif curr_sum==M:
        curr_sum -= nums[start]
        cnt+=1
        start+=1
        
    else:
        if end>=N:
            break
        else:
            curr_sum+=nums[end]
            end+=1

print(cnt)