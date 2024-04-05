import itertools
N,M=map(int,input().split())

nums=list(range(1,N+1))
permu=list(itertools.permutations(nums,M))
for i in permu:
  print(' '.join(map(str, i)))