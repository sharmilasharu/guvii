Number1=(input(""))
number=Number1.split()
a=int(number[0])
b=int(number[1])
for i in range(a+1,b):
  if((i%2)!=0):
    print(i,end=" ")
