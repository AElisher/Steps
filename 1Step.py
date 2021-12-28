first_number = float(input("Pick the first number: "))

operation = input("Choose the operation(+, -, *, /): ")

second_number = float(input("Pick the second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number    
else:
    print("Choose appropriate operation")

print("Result: " + str(result))