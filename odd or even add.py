a=[]
size=int(input("Entar the size of list= "))
for i in range(size):
  val=int(input("Enter the number for list="))
  a.append(val)
Even=0
odd=0
for i in range(size):
 if(a[i]%2==0):
  Even=Even+1
 else:
   odd=odd+1
print("tatal number of Even=",Even,"tatal number of Even=",odd)