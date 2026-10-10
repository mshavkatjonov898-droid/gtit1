# correct_username = "admin"
# correct_password = "1234"
# attempts = 0

# while attempts < 3:
#     username = input("Login kiriting: ")
#     password = input("Parol kiriting: ")

#     if username == correct_username and password == correct_password:
#         print("Xush kelibsiz, tizimga kirdingiz!")
#         break
#     else:
#         print("Login yoki parol noto'g'ri. Qaytadan urinib ko'ring.")
#         attempts += 1

# if attempts == 3:
#     print("Uch martadan ko'p urinish. Tizim bloklandi.")

# users = [
#     {
#         "login": "ali",
#         "password": "12",
#     },
#     {
#         "login": "vali",
#         "password": "123",
#     },
#     {
#         "login": "vali",
#         "password": "124",
#     }
# ]

# stop = False

# while True:

#     if stop:
#         break

#     login = input()
#     parol = input()

#     for i in users:
#         if i["login"] == login and i["password"] == parol:
#             print("Muvaffaqiyatli tizimga kirdingiz")
#             stop = True
#             break


# qalinlik = 0.0000001
# masofa = 384400
# buklash = 0

# while True:
#     qalinlik *= 2
#     buklash += 1
#     if qalinlik >= masofa:
#         break
# print(buklash)


# def log2_exact_power(x):
#     if x <= 0 or (x & (x - 1)) != 0:
#         raise ValueError("This method only works for exact powers of 2.")
        
#     count = 0
#     while x > 1:
#         x //= 2
#         count += 1
#     return count

# log2_exact_power(masofa/qalinlik)
# import math

# thickness = 0.0001
# distance_to_moon = 384400000

# folds = math.ceil(math.log2(distance_to_moon / thickness))
# print(f"{folds}")

# import random
# number_to_guesss = random.randint(1, 101)
# guess = 0

