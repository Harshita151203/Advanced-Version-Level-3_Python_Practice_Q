# 1. Take multiple names in one input and display them sorted alphabetically.

multi_input = input("Enter: ").lower()
new = multi_input.split()

new.sort() 
print("Sorted Names: ")

for  names in new: 
    print(names) 

