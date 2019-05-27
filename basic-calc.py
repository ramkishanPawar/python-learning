"""@author: Ramkishan K Pawar
Python program to do basic calculations """

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

print("1. Addition. ")
print("2. Substraction. ")
print("3. Multiplication. ")
print("4. Division. ")
choice = int(input("Enter Your Choice: "))

if choice == 1:
    addition = num1 + num2
    print("The Sum of {} and {} is: {}".format(num1,num2,addition))

elif choice == 2:
    sub = num1 - num2
    print("The Substraction of {} and {} is: {}".format(num1,num2,sub))

elif choice == 3:
    mul = num1 * num2
    print("The Multiplication of {} and {} is: {}".format(num1,num2,mul))

elif choice == 4:
    try:
        div = num1 / num2
        print("The division of {} and {} is: {}".format(num1,num2,div))
    except ZeroDivisionError:
        print("Dividing by Zero, Try Again !!")
        
else:
    print("Please, check if you have entered numbers !")

