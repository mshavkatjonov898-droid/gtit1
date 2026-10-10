# # 1-vazifa

# age = int(input("Enter your age: "))

# if age < 7:
#     print("Kindergarten")
# elif age < 18:
#     print("School")
# elif age < 22:
#     print("University")
# else:
#     print("Work")

# # 2-vazifa

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Divisible by 2")
# if number % 5 == 0:
#     print("Divisible by 5")
# if number % 10 == 0:
#     print("Divisible by 10")

# # 3-vazifa

# login = input("Enter your login: ")

# if login == "admin":
#     password = input("Enter your password: ")
#     if password == "1234":
#         print("Welcome")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect login")


# # 4-vazifa

# weather_celcius = float(input("Enter the temperature in Celsius: "))

# if weather_celcius > 26:
#     print("Get the air conditioner")
# elif weather_celcius < 0:
#     print("Wear warm clothes")
# else:
#     print("Chill")

# # 5-vazifa

# ball = float(input("Ballni kiriting (0-100): "))

# if ball < 0 or ball > 100:
#     print("Xato ball!")
# elif ball >= 90:
#     print("5 (A'lo)")
# elif ball >= 70:
#     print("4 (Yaxshi)")
# elif ball >= 56:
#     print("3 (Qoniqarli)")
# else:
#     print("Yiqildi")

# # 6-vazifa

# 1.

# battery_percentage = int(input("Enter battery percentage: "))

# plugged_in = input("Is the charger plugged in? (yes/no): ").strip().lower()

# if battery_percentage > 20 or plugged_in == "yes":
#     print("You can use the phone.")
# else:
#     print("You cannot use the phone.")

# 2.

# money_amount = float(input("Enter the amount of money you have: "))

# have_ticket = input("Do you have a ticket? (yes/no): ").strip().lower()

# if money_amount >= 50000 and have_ticket == "yes":
#     print("You can enter the concert.")
# else:
#     print("You cannot enter the concert.")

# # 7-vazifa

# age = int(input("Enter your age: "))

# has_job = input("Do you have a job? (yes/no): ").strip().lower()

# income = float(input("Enter your monthly income: "))

# is_in_blacklist = input("Are you in the blacklist? (yes/no): ").strip().lower()

# if age > 22 and has_job == "yes" and income > 5000000 and is_in_blacklist == "no":
#     print("You can get a loan.")
# else:
#     print("You cannot get a loan.")

# # 8-vazifa

# email = input("Enter your email: ")

# if "@" in email and email.endswith(".com"):
#     print("Email to'g'ri")
# else:
#     print("Email noto'g'ri")

# # 9-vazifa

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# mo = input("Enter the math operation (+, -, *, /): ")
# try:
#     if mo == "+":
#         print(num1 + num2)
#     elif mo == "-":
#         print(num1 - num2)
#     elif mo == "*":
#         print(num1 * num2)
#     elif mo == "/":
#         print(num1 / num2)
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas!")
# except NameError:
#     print("Bunday amal yo'q!")