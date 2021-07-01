# Hero's Inventory 3.0
# Demonstrates lists

# create a list with some items and display with a for loop
# lists are mutable and can be changed
# tuples are immutable and cannot be changed

# Indexes start at 0
inventory = ["sword", "armor", "shield", "healing potion"]

# get the length of a list
# print("You have", len(inventory), "items in your possession.")

# input("\nPress the enter key to continue.")

# test for membership with in
# if "healing potion" in inventory:
#     print("You will live to fight another day.")

# display one item through an index
# position = int(input("\nEnter the position for an item in inventory: "))

# index = position - 1

# check to see if index is in range
# if index < 0 or index >= len(inventory):
#     print("Invalid index!")
# else:
#     print("At position", position, "is", inventory[index])

# display a slice
# start = int(input("\nEnter the index number to begin a slice: "))
# finish = int(input("Enter the index number to end the slice: "))
# print("inventory[", start, ":", finish, "] is", end=" ")
# print(inventory[start:finish])

# input("\nPress the enter key to continue.")


# 1. change elements of the inventory list
inventory[0] = "crossbow"


# 2. Replace the first two elements starting at the index of 1 with two new elements

# inventory[1] = "coins"
# inventory[2] = "map"

# 3. Remove the element at the the index of 3 (use remove() method)
# inventory.pop(3)


# 4. Allow the user to specify the value they wish to delete from the list and then
# delete the value from the list

print("Your items:")
for item in inventory:
		print(item)

specifiedItem = input("What item would you like to remove from your inventory? ")

while specifiedItem not in inventory:
	specifiedItem = input("Please choose a valid item that is in your inventory ")

for item in inventory:
	if item == specifiedItem:
		inventory.remove(item)

print("Successfully removed item \"" + specifiedItem + "\" from your inventory")

# 5. Add a new element to the end of the list
# inventory.append("shield")

print("New inventory:")
for item in inventory:
		print(item)
