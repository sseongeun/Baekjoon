def solution(phone_number):
    phone_number=list(phone_number)
    
    last="".join(phone_number[-4:])
    print(last)
    
    front="*" * (len(phone_number)-4)
    print(front)
    
    answer=front+last
    return answer
   
        