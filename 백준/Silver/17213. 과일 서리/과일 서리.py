def factorial(num):
    if(num>1):
        return num*factorial(num-1)
    else:
        return 1
    
N=int(input())
M=int(input())
top=factorial(M-1)
bottom=factorial(M-N)*factorial(N-1)
print(top//bottom)