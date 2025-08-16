a=int(input("Enter the 1st sub number"));
b=int(input("Enter the 2nd sub number"));
c=int(input("Enter the 3rd sub number"));
d=int(input("Enter the 4th sub number"));
e=int(input("Enter the 5th sub number"));
total=a+b+c+d+e
persent=(total/500)*100
print("total number=",total); 
print("persent=",persent);
if persent>=80:
  print("got the first devison");
elif persent>=60:
   print("got the second devison");
elif persent>=40:
  print("got the third divisiaon");
else persent>=40: 
  print ("failed")