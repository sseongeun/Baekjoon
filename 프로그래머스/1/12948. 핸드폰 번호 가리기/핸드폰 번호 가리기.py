def solution(phone_number):
    length = len(phone_number)
    remain = phone_number[-4:]
    front  = "*"*(length-4)
    
    return front+remain
