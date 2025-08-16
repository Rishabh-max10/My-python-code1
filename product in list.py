a=[]
size=int(input("Entar the size of list= "))
for i in range(size):
  val=int(input("Enter the number for list="))
  a.append(val)
Even=0
prod=1
for i in range(size):
 if(a[i]%2==0):
  Even=Even+(a[i])
 else:
   prod=prod*(a[i])
print("tatal number of Even=",Even,"tatal  prod=",prod)