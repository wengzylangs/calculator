 # simple calculator app
print('''************
1. Adiition
2. Subtraction
3. Multiplication
4. Division
5. exponential

********''')
print("Enter two numbers to add")
# prompt a user for a number and store it 
first_num = input("first_num: ")
# prompt a user for number and store it
second_num = input("second_num: ")
sum = float(first_num) + float(second_num)
print(f"{first_num} + {second_num}= {sum}")

print('''**************
subtraction
*********''')

print("Enter two numbers to subtract")
# prompt a user for a number and store it 
first_num = input("first_num: ")
# prompt a user for number and store it
second_num = input("second_num: ")
sub = float(first_num) - float(second_num)
print(f"{first_num} - {second_num}= {sub}")

print('''*******
Multiplication''')
#prompt a user for a number and multiply
first_num = input("first_num:")
# prompt a user for a number and store it
second_num = input("second_num")
mul = float(first_num) * float(second_num)
print(f"{first_num} * {second_num} = {sum:,.2f}")

print('''********
exponential
*****''')
#prompt a user for a number and exponent
first_num = input("first_num:")
# prompt a user for a number and store it
second_num = input("second_num")
exp = float(first_num) ** float(second_num)
print(f"{first_num} ** {second_num} = {exp:,.2f}")

