my_list = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "gray", "pink", "indigo", "brown", "tan", "gold", "silver"]
gep = 0

letter = input("instert 1 letter: ")

inspector = "There are {} items in the list that have the letter {} in it."

for x in my_list:
    if letter in x:
        gep = gep + 1
print(inspector.format(gep,letter))
#for x in my_list:
