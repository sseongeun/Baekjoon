from collections import Counter



def solution(participant, completion):

    counter = Counter(participant)-Counter(completion)
    return ''.join(list(counter))