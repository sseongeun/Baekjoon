import sys
input=sys.stdin.readline

S,E,Q = map(str,input().split()) # 시작 시각, 끝난 시각, 스트리밍 끝난 시각

in_list=set()
out_list=set()
cnt=0

while True:
    try:
        time,name=map(str,input().split())
        
        if time<=S:
            in_list.add(name)
        elif name in in_list and E<=time<=Q:
            out_list.add(name)
    except:
        break
        
print(len(out_list))