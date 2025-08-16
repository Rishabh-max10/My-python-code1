a=int(input("Enter the 1st number"));
b=int(input("Enter the 2nd number"));
c=int(input("Enter the 3rd number"));
if (a>b and a<c)or(a<b and a>c): 
    print ("the number is middle=",a);
elif(b>a and b<c) or(b<a and b>c):
    print ("the number is middle=",b);
else:
    print("the number is middle=",c);   