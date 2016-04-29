from Item import Item

print "Amazon Scraper: Where all your frugal dreams come true.\n"

choice = 0

while choice != 4:
	print "1. Define new item\n"
	print "2. Check current items\n"
	print "3. Delete an item\n"
	print "4. Exit\n"

	choice = raw_input("Please select an option by entering a number, 1 through 4 :")

	try:
		choice = int(choice)
	except ValueError:
		print "Error: input not numeric. Please try again!\n"
		continue

	if (choice < 0) or (choice > 4):
		print "Error: choice not defined. Please try again!\n"

	elif choice == 1:
		print "Define new item\n"
		 #define new item here
     	elif choice == 2:
		print "Check item\n"
		 #check items here
	elif choice == 3:
		print "Delete an item\n"
		 #delete an item here
	else:
		print "Exiting now..."

