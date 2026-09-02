#defining a varibale
"""snake_case_variable = "This is a snake case variable"
print(snake_case_variable)"""

'''a = "COLLEGE"
print(a)

print(a[3:6])  # This will print characters from index 3 to 5 (6 is not included)
print(a[3:6:2])  # This will print characters from index 3 to 5 with a step of 2
print(a[0:7:2])  # This will print characters from index 0 to 6 with a step of 2
print(a[::2])  # This will print every second character from the entire string  

a = "Hello how are you?"

print(a[6:9:1],"\n", a[14:17:1],"\n", a[0:5:1])  # This will print "how you Hello"'''

#limitations
# a = '12.2'
# a =float(a)
# a=int(a)
# print(a)

# age = int(input("Enter your age: "))

# print("Your age is:", age)
# print(f"Your age is: {age}")


# practice 1

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num1} is less than {num2}")
# else:
#     print(f"{num1} is equal to {num2}")

# practice 2

# gender = input("Enter your gender (M/F): ").strip().upper()
# if gender == "M":
#     print("You are a male.")
# elif gender == "F":
#     print("You are a female.")
# else:
#     print("Invalid input.")


# practice 3

# year = int(input("Enter a year: "))
# if year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year.")     
# elif year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# temp = int(input("Enter the temperature in Celsius: "))
# if temp >= -5 and temp <= 5:
#     print("The weather is very cold.")
# elif temp > 5 and temp <= 15:
#     print("The weather is cool.")
# elif temp > 15 and temp <= 25:
#     print("The weather is warm.")
# else:
#     print("The weather is hot.")


# n =int(input("Enter a number to get the multiplication table: "))
# for i in range(n,(n*10)+1,n):
#     print(i)

# a= "Students"
# for i in range(len(a)):
#         print(f"{i}: {a[i]}")


# factorial = 1
# n = int(input("Enter a number to calculate its factorial: "))
# for i in range(1, n + 1):
#     print(i)
#     factorial = factorial * i
# print(f"The factorial of {n} is {factorial}")



# nums = int(input("Enter the number : "))
# even_sum = 0
# odd_sum = 0

# for i in range(1, nums + 1):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

# print(f"The even sum is {even_sum}")
# print(f"The odd sum is {odd_sum}")

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(f"{i} is a factor of {n}")


num = int(input("Enter a number: "))

perfect_sum = 0

for i in range(1, num):
    if num % i == 0:
        perfect_sum += i  

if  num == perfect_sum:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")