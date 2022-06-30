def rev(a):
    su=0
    while a>0:
        rem=a%10
        su=(su*10)+rem
        a//=10
    return su
a=int(input())
print(rev(a))