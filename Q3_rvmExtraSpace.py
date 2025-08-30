# Read a sentence and remove all extra spaces (multiple spaces → single space)

mysent = input("Enter: ")
new = " ".join(mysent.split()) 
print(new)  