# 1
#
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Please enter a number")

# 2
#
# try:
#     num = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     print(num / num2)
# except ValueError:
#     print("Please enter a number")
# except ZeroDivisionError:
#     print("Impossible to divide by zero")

# 3
#
# mevalar = ["olma", "anor", "uzum"]
#
# try:
#     index1 = int(input("Enter an index: "))
#     print(mevalar[index1])
# except ValueError:
#     print("Please enter a number")
# except IndexError:
#     print("Nothing found")

# 4
#
# capitals = {
#     "Turkey": "Ankara",
#     "Uzbekistan": "Tashkent",
#     "China": "Beijing",
#     "Russia": "Moscow",
# }
#
# country = input("Enter country name: ")
# print(capitals.get(country))
#
# try:
#     country = input("Enter country name: ")
#     print(capitals[country])
# except KeyError:
#     print("Country not found")

# 5
#
# while True:
#     try:
#         number = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Please enter a number")

# 6
#
# try:
#     yosh = int(input("Yoshingizni kiriting: "))
#
#     if yosh < 0:
#         raise ValueError("Yosh manfiy bo'lmaydi!")
#     elif yosh > 150:
#         raise ValueError("Buncha yashab bo'lmaydi!")
#
#     print(f"Kiritilgan yosh: {yosh}")
#
# except ValueError as e:
#     print(f"Xatolik: {e}")

# 7
#
# balans = 100000
#
# try:
#     summa = float(input("Yechmoqchi bo'lgan summani kiriting: "))
#
#     if summa > balans:
#         raise Exception("Balansda yetarli mablag' mavjud emas!")
#
#     balans -= summa
#     print(f"Pul yechildi. Qolgan balans: {balans} so'm")
#
# except ValueError:
#     print("Xatolik: Iltimos, faqat son kiriting!")
# except Exception as e:
#     print(f"Xatolik: {e}")
# finally:
#     print("Operatsiya yakunlandi")

# 8
# #
# kiritilgan = input("Vergul bilan sonlar kiriting (masalan: 5, 8, 12): ")
# elementlar = kiritilgan.split(",")
#
# sonlar = []
# xatolik_bor = False
#
# for item in elementlar:
#     tozalangan = item.strip()
#     try:
#         son = int(tozalangan)
#         sonlar.append(son)
#     except ValueError:
#         print(f"Xato qiymat topildi: '{tozalangan}' (butun son emas)")
#         xatolik_bor = True
#
# if not xatolik_bor and sonlar:
#     ortacha = sum(sonlar) / len(sonlar)
#     print(f"Sonlarning o'rtacha qiymati: {ortacha}")
# elif xatolik_bor:
#     print("Xatoliklar sababli o'rtacha qiymat hisoblanmadi.")