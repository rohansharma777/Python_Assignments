print("To 'Add' two numbers press 1")
print("To 'Multiply' two numbers press 2")
print("To 'Subtract' two numbers press 3")
print("For 'Division' press 4")
y=1
n=0
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
	else:
	    print("'Dividing' 1st no. by 2nd no. : ",x/y)
	cont=bool(input("Do you want to continue ? (y/n)"))