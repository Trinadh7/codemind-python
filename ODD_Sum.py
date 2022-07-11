n=int(input())
a=list(map(int,input().split()))
s=a[0]
s1=0
for i in range(n):
    if a[i]%2==0:
        s=s+a[i]
    else:
        s1=s1+a[i]
print(s1)