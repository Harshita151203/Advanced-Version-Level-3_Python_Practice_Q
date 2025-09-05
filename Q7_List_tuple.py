# 7. Accept comma-separated numbers and
#  convert them into both list and tuple.

var = input("Enter Numbers : ")
new = var.split(",")

mylist = [int(x) for x in new]
mytup = tuple(mylist)
print("List: ",mylist)  
print("Tuple: ",mytup)  
   
    
