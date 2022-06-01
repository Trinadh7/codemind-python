(a,b)=map(int,input().split())
n=list(map(int,input().split()))
c=0
for i in range(a):
    if n[i]%b==0:
        c+=1
print(abs(c-a))