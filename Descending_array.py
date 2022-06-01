n=int(input())
a=list(map(int,input().split()))
k=a[::-1]
b=sorted(a)
if k==b:
    print("yes")
else:
    print("no")