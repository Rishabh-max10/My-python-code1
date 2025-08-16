a=int(input("Enter a number"));
sum=0
prod=1
While(a>0)
d=a%10
if d%2==0:
   sum=sum+d
else:
    prod=prod*d
    a=a//10
    
    print("sum of the number=",sum);
    print("product og the number=",prod);
         