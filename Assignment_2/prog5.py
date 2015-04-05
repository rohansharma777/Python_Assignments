gender = input("Enter you gender.m - for male and f - for female")
salary = int(input("Enter your current salary"))
if gender == 'm' and salary < 1000:
    bonus = salary + (salary * 5 / 100)
    print("Salary after recieving bonus.: ", bonus)
elif gender == 'f' and salary < 1000:
    bonus = salary + (salary * 5.5 / 100)
    print("Salary after recieving bonus.: ", bonus)
elif salary > 1000:
    bonus = salary + (salary * 5 / 100)
    print("Salary after recieving bonus.: ", bonus)
