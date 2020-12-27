users = ["ahmed","mohamed","mahmoud","toni","reda","osama"]
name = input("enter your name: ")
if name in users:
	print(f"welcome {name} again")
	option = input("Do you want to remove or update yor name [ r - u ]")
	if option == ("u") :
		update = input("Ok type your new name: ")
		users[users.index(name)] = update
		print("The name is updated")
		
	elif option == ("r") :
		users.remove(name)
		print("Name has been removed")
	
	else:
		print("Wrong option")
	
else:
	print(f"{name}, you are not admin" )
	option = input("Do you want to be admin [ y - n ]: ")
	if option == ("y") :
		users.append(name)
		print("You have been add")
	
	elif option == ("n") :
		print("Ok, thank you")