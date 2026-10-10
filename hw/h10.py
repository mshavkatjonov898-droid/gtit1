# 1.

# n = 10

# while n >= 0:
#     print(n)
#     n -= 1
# print("Parvoz! 🚀")

# 2.

# N = 0

# while True:
#     n = int(input("Son kiriting (to'xtash uchun 0 ni kiriting): "))
#     N += n
#     if n == 0:
#         break
# print(f"Jami: {N}")

# 3.

# N = 100
# K = 4

# b = 0
# q = N

# while q >= K:
#     q -= K
#     b += 1

# print("Butun qismi:", b)
# print("Qoldig'i:", q)

# 4.

# n = int(input(">>>"))
# while n > 1 and n % 3 == 0:
#     n //= 3

# if n == 1:
#     print("3 ning darajasi")
# else:
#     print("3 ning darajasi emas")

# 5.

# n = int(input())
# k = 0

# while n >= 2 and n % 2 == 0:
#     n //= 2
#     k += 1
# print(k)

# 6.

# n = 50
# k = 0

# while k * k <= n:
#     k += 1

# print(k)

# 7.

# n = int(input("n ni kiriting: "))
# s = 0
# k = 0

# while s < n:
#     k += 1
#     s += k

# print(k)
# print(s)

# 8.

# s = float(input())
# p = int(input())
# o = 0
# sum1 = s

# while sum1 <= s * 2:
#     sum1 += sum1 * p/100
#     o += 1

# print(o)
# print(s)

# 10.

# kontaktlar = {}

# while True:
#     choice = input("1 — kontakt qo'shish, 2 — qidirish, 3 — chiqish: ")
#     if choice == "1":
#         kontakt = input("Kontakt ismini kiriting: ")
#         raqam = input("Kontakt raqamini kiriting: ")
#         kontaktlar[kontakt] = raqam
#         print(f"{kontakt} saqlandi.")
#     elif choice == "2":
#         kontakt = input("Qidirilayotgan kontakt ismini kiriting: ")
#         if kontakt in kontaktlar:
#             print(f"{kontakt}: {kontaktlar[kontakt]}")
#         else:
#             print("Bunday kontakt topilmadi.")
#     elif choice == "3":
#         break