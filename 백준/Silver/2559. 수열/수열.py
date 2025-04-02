N,K=map(int,input().split()) # 수의 개수, 연속된 일자수
nums = list(map(int,input().split()))

start =0
end = K-1
curr_sum = sum(nums[start:end+1])
max_nums=[]
max_nums.append(curr_sum)

while end<N-1:
    curr_sum = curr_sum-nums[start]+nums[end+1]
    max_nums.append(curr_sum)
    start+=1
    end+=1
    
print(max(max_nums))