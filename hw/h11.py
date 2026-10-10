# 1.

# def greeting(name):
#     return f"Assalomu alaykum, {name}!"

# print(greeting("ism"))

# 2.

# def kvadrat(num):
#     return num **2
# def kub(num):
#     return num **3
# print(kvadrat(5) + kub(2))

# 3.

# def katta_son(a, b):
#     return max(a, b)
# print(katta_son(5, 6))

# 4,

# def fahr_to_celsius(temp):
#     return (temp - 32) * 5/9
# print(fahr_to_celsius(32))

# 5.

# def juftmi(son):
#     return son % 2 == 0
# print(juftmi(7))

# 6.

# def chegirma(narx, foiz=10):
#     return narx * foiz/100
# print(chegirma(80, foiz=50))

# 7.

# def ortacha(*args):
#     return sum(args)/len(args)
# print(ortacha(5, 4, 5))

# 8.

# def anketa(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{kalit}: {qiymat}")
# anketa(ism="Ali", sinf=9, shahar="Toshkent")

# 9.

# def baho(ball):
#     if ball > 100 or ball < 0:
#         return "Noto'g'ri ball!"
#     elif 100 >= ball >= 90:
#         return "A'lo"
#     elif ball >= 70:
#         return "Yaxshi"
#     elif ball >= 60:
#         return "Qoniqarli"
#     else:
#         return "Yiqildi"
# print(baho(101))

# 10.

# def kalkulyator(a, amal, b):
#     if amal == "+":
#         return a + b
#     elif amal == "-":
#         return a - b
#     elif amal == "*":
#         return a * b
#     elif amal == "/":
#         if b == 0:
#             return "Xato!"
#         return a / b
#
# while True:
#     amal = input("Amalni kiriting (+, -, *, /) yoki chiqish uchun 'stop' deb yozing: ").strip()
#
#     if amal.lower() == "stop"
#         print("Break")
#         break
#     if amal not in ["+", "-", "*", "/"]:
#         print("Xato: Bunday amal mavjud emas!")
#         continue
#
#     try:
#         a = float(input("Birinchi sonni kiriting: "))
#         b = float(input("Ikkinchi sonni kiriting: "))
#     except ValueError:
#         print("Xato: Faqat son kiritishingiz kerak!")
#         continue
#
# natija = kalkulyator(a, amal, b)
# print(f"Natija: {natija}")