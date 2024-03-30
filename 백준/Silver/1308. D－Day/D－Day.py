import datetime

a=list(map(int,input().split()))
b=list(map(int,input().split()))

start=datetime.date(a[0],a[1],a[2])
thou=datetime.date(a[0]+1000,a[1],a[2])
end=datetime.date(b[0],b[1],b[2])

result=(end-start).days
if end>=thou:
    print("gg")
else:
    print("D-{}".format(result))


