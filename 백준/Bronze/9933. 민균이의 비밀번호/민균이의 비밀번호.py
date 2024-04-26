N=int(input())
pw=[]
for i in range(N):
    pw.append(input())
for i in range(N):
    if pw[i][::-1] in pw:
        l=len(pw[i])
        print(l,pw[i][l//2])
        break
