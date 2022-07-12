def pal(n):
   t=n
   a=0 
   while(n):
       d=n%10
       a=a*10+d
       n=n//10
   if  (a==t):
         return 1
   else:
        return 0
n= int(input())
for i in range(n+1,100000):
    if pal(i):
        a=i
        break
for i in range(n-1,0,-1):
    if pal(i):
        a1=i
        break
if abs(a1-n)==abs(a-n):
    print(a1,a)
elif abs(a1-n)<abs(a-n):
    print(a1)    
else:
    print(a)