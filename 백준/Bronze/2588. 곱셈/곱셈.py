A=int(input())
B=int(input())

f1=A*(B%10)
f2=A*(B%100-B%10)//10
f3=A*(B//100)

print(f1)
print(f2)
print(f3)
print(f1+10*f2+100*f3)