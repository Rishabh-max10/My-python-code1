a=int(input("Enter aa number"));
sum=0
orig=a
while(a>0):
    sum=sum+(a%10)*(a%10)*(a%10)
    a=a//10
if orig==sum:
    print("This is a armstrong number");
else:
   print("This is a not armstrong number");
        