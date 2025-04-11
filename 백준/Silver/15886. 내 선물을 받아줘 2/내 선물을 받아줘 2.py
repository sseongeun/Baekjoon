
N=int(input())
map_list=list(input())


cnt=0
for i in range(N-1):
    if "".join(map_list[i:i+2])=="EW":
        cnt+=1

print(cnt)