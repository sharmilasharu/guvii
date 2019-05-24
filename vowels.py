let=input("Enter the let: ")
if((let>"a" and let<"z" )or( let>"A"  and let<"Z")):
  if(let=="a"or let=="e" or let=="i"or let=="o" or let=="u" or let=="A"or let=="E" or let=="I" or let=="O" or let=="U"):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")    
