N,M = map(int,input().split())

n_list=[]
m_list=[]

for _ in range(N):
    n_list.append(input())
    
for _ in range(M):
    m_list.append(input())
    
common= list(set(n_list)&set(m_list))
common.sort()

print(len(common))
for c in common:
    print(c)