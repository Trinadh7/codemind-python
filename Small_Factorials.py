def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f
t=int(input())
for i in range(t):
    a=int(input())
    print(fact(a)),