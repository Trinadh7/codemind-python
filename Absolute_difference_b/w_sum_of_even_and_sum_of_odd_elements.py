n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in range(0,n):
    if a[i]%2==0:
        s=s+a[i]
    else:
        s1=s1+a[i]
print(abs(s-s1))