import sys
import itertools
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(str, input().split()))
le = len(str(n))

while True:
	# iterables에 있는 모든 요소들의 조합을 만들어내는 반복자 생성.
	a = list(itertools.product(arr,repeat=le))
	result = []
	# 모든 요소들의 조합 중 n보다 작은 값을 모두 구해 result 배열에 넣습니다.
	for i in a:
		temp = int(''.join(i))
		if n >= temp:
			result.append(temp)
	# 만약 값이 없다면 같은 자리 수 중에 n보다 작은 수가 없는 것으로 판단해 자리 수를 줄입니다.
	if len(result) >=1:
		print(max(result))
		break
	else:
		le-=1
        