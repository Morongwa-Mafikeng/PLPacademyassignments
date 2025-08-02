#input numbers to operate on and the operation 

number_1 = int(input("Enter the first value: "))
number_2 = int(input("Enter the second value: "))
op = input("Enter the operation: ")


if op == '+':
    print("The sum of two numners = ", number_1 + number_2) # adding the two numbers
elif op == '-':
    print("The difference of two numners = ", number_1 - number_2) #subtracting the two numbers
elif op == '*':
    print("The product of two numners = ", number_1 * number_2) # Multiplying the two numbers
elif op == '/':
    print("The division of two numners = ", number_1 / number_2) # Division the two numbers
