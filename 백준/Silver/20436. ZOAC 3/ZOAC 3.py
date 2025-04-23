import math

keyboard = {'q':(0,0),'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4),'y':(0,5),'u':(0,6),'i':(0,7),'o':(0,8),'p':(0,9),
            'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),
            'z':(2,0),'x':(2,1),'c':(2,2),'v':(2,3),'b':(2,4),'n':(2,5),'m':(2,6)}

start_left, start_right = map(str,input().split())
key_list=list(input())

curr_left=list(map(int,keyboard[start_left]))
curr_right=list(map(int,keyboard[start_right]))
total=0

for key in key_list:
    total+=1
    curr = list(map(int,keyboard[key]))
    if curr[1]<=4:
        if curr == [2,4]:
            total+=abs(curr_right[0]-curr[0])+abs(curr_right[1]-curr[1])
            curr_right=curr
        else:
            total+=abs(curr_left[0]-curr[0])+abs(curr_left[1]-curr[1])
            curr_left=curr
    else:
        total+=abs(curr_right[0]-curr[0])+abs(curr_right[1]-curr[1])
        curr_right=curr
        
print(total)