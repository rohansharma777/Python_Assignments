print("To 'Add' two numbers press 1")
print("To 'Multiply' two numbers press 2")
print("To 'Subtract' two numbers press 3")
print("For 'Division' press 4")
<<<<<<< HEAD
cont=True 
while cont == True:
	choice=int(input("Enter your choice.: "))
	if choice < 1 or choice > 4:
	    print("Sorry bad choice. Please enter a valid choice")
	else:
		x=int(input("Enter your first no.: "))
		y=int(input("Enter your second no.: "))
		if choice == 1:
		    print("The 'Addition' of both the no.s is : ",x+y)
		elif choice == 2:
		    print("The 'Multiplication' of both the no.s is : ",x*y)
		elif choice == 3:
		    print("'Subtracting' the 2nd no from 1st no. : ",x-y)
		elif choice == 4:
			print("'Dividing' 1st no. by 2nd no. : ",x/y)
	c=input("Do you want to continue ? (y/n) :  ")
	if c== 'y':
		cont = True
	else:
	 	cont = False
=======
cont=True
while cont == True:
	choice=int(input("Enter your choice.: "))
	x=int(input("Enter your first no.: "))
	y=int(input("Enter the second no.: "))
	if choice == 1:
		print("The 'Addition' of both the no.s is : ",x+y)
	elif choice == 2:
		print("The 'Multiplication' of both the no.s is : ",x*y)
	elif choice == 3:
		print("'Subtracting' the 2nd no from 1st no. : ",x-y)
	elif choice == 4:
	    print("'Dividing' 1st no. by 2nd no. : ",x/y)
	else:
	    print("OOPS! it seems like you have entered a wrong choice !") 	
	c=input("Do you want to continue ? (y/n)")
	if c == 'y':
	    cont=False
	else:
	    cont=True	
>>>>>>> fefbb3126cccf7b566a08e7b29fc2edffaabd9c2
