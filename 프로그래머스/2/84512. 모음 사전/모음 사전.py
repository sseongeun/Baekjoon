from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    vocas=[]


    for i in range(1, 6):
        for j in product(vowels, repeat=i): 
            vocas.append( ''.join(j))
            
    vocas=sorted(vocas)
    return vocas.index(word)+1
        