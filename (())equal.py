inpout=input("")
starting=0
ending=0
for i in inpout:
  if(i=="("):
    starting=starting+1
  elif(i==")"):
    ending=ending+1

if(starting==ending):
  print("yes")
else:
  print("no")  
