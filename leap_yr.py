num=int(input())
if(num%4==0 and num%100!=0):
  print("yes")
elif(num%400==0):
  print("yes")
else:
   print("no")   
