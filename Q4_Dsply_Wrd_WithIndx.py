# Accept a sentence and display each word with its index number

mysent = input('Enter: ')
new = mysent.split()

for index, my in enumerate(new):
    print("Index:",index, "Word:",my)  