def find(parent,x): 
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    root_a = find(parent,a)
    root_b = find(parent,b)
    if root_a != root_b:
        parent[root_b] = root_a
        


def solution(n, costs):
    sorted_cost = sorted(costs, key =lambda x:x[2])
    parent = [ i for i in range(n)]

    total_cost=0
    edges_used=0

    for a,b,cost in sorted_cost:
        if find(parent,a) != find(parent,b): 
            union(parent,a,b)
            total_cost += cost
            edges_used+=1

            if edges_used == n:
                break

    return total_cost
    