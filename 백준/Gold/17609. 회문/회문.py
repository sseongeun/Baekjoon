def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def check_str(voca,start,end):
    
    while start<end:
        if voca[start]!=voca[end]:
            if is_palindrome(voca,start+1,end) or is_palindrome(voca,start,end-1):
                return 1
            else:
                return 2
            
        start+=1
        end-=1
        
    return 0


T=int(input())

for _ in range(T):
    input_str = input()
    print(check_str(input_str,0,len(input_str)-1))