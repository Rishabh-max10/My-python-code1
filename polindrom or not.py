#Writeba program to check number is polindrom or not
a=input("Enter the number")
b=a[-1::-1]
if(a==b):
  print ("the number is polindrom");
else: 
  print ("the number is not polindrom");