a=int(input("Enter The Number :"));
prod=1
while (a>0):
    prod=prod*(a%10)
    a=a//10
print ("this is a product=",prod);   