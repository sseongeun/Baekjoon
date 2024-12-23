def solution(s):
    numList= ['1','2','3','4','5','6','7','8','9','0']

    if len(s)==4 or len(s)==6:
        for i in s:
            if i not in numList:
                return False

        return True
    else:
        return False