#PF-Assgn-3
#This verification is based on string match.

mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five=True

#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
per_head_cost=(((distance_one_way*2)/(mileage))*(amount_per_litre))/4





#Do not modify the below print statements for verification to work
print(per_head_cost)
if(per_head_cost%5==0):
    print(divisible_by_five)
else:
    print("False")
