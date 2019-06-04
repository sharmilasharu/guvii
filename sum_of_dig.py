number=int(input())
sum=0
while(number!=0):
  remainder=number%10
  sum=sum+(remainder**2)
  number=number//10
print(sum)  
  
