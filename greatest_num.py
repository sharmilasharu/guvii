num=(input())
var=num.split()
num1=int(var[0])
num2=int(var[1])
num3=int(var[2])
if(num1>num2 and num1>num3):
  print(num1)
elif(num2>num3 and num2>num1): 
  print(num2)
elif(num3>num1 and num3>num2):
  print(num3)  
else:
  print("invalid")  
