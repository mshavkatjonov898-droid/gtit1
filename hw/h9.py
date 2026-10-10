# 1.

# words = {
#     "olma": "apple",
#     "anor": "pomegranate",
#     "banan": "banana",
#     "shaftoli": "peach",
#     "qulupnay": "strawberry",
# }

# word = input("Enter a word in Uzbek: ")

# if word in words:
#     print(f"The English translation of '{word}' is '{words.get(word)}'.")
# else:
#     print(f"Sorry, the word '{word}' is not in the dictionary.")

# 2.

# telefon_daftari = {}

# for i in range(3):
#     ism = input(f"{i+1}-kontakt ismini kiriting: ")
#     raqam = input(f"{ism}ning telefon raqamini kiriting: ")
#     telefon_daftari[ism] = raqam

# print("Saqlangan kontaktlar")

# for ism, raqam in telefon_daftari.items():
#     print(f"{ism} - {raqam}")

# 3.

# oquvchi = {
#     "ism": "Ali",
#     "yosh": 15,
#     "sinf": "9-A"
# }

# oquvchi["shahar"] = "Toshkent"

# oquvchi["yosh"] += 1

# del oquvchi["sinf"]

# for kalit, qiymat in oquvchi.items():
#     print(f"{kalit.title()}: {qiymat}")

# 4.

# participation = {
#     "Ali": True,
#     "Vali": False,
#     "Gani": True,
#     "Qani": False,
#     "Sani": True,
# }

# N = 0
# for key, value in participation.items():
#   if value == True:
#     N += 1
# print(f"Bugun {N} ta o'quvchi keldi")

# 5.

# prices = {"non": 4000, "sut": 15000, "tuxum": 18000}

# list_shopping = ["non", "sut", "non"]

# summa = 0

# for i in list_shopping:
#   for key, value in prices.items():
#     if i == key:
#       summa = value + summa
# print(summa)

# 6.

# pupils = {"Ali": [5, 4, 5], "Laylo": [4, 4, 3]}

# for key, value in pupils.items():
#   print(f"""{key} average ball {sum(value)/len(value)}""")

# 7.

# sonlar = [3, 7, 3, 1, 7, 7, 9, 1]

# print(set(sonlar))

# print(len(sonlar) - len(set(sonlar)))

# 8.

# futbolchilar = {"Ali", "Vali", "Hasan", "Umar", "Sardor"}

# shaxmatchilar = {"Hasan", "Umar", "Bekzod", "Jasur"}

# ikkalasiga_ham = futbolchilar.union(shaxmatchilar)

# faqat_futbol = futbolchilar.difference(shaxmatchilar)

# barcha_bolalar = futbolchilar.intersection(shaxmatchilar)

# print("(a) Ikkalasiga ham qatnaydiganlar:", ikkalasiga_ham)

# print("(b) Faqat futbolga qatnaydiganlar:", faqat_futbol)

# print(f"(c) To'garaklarga qatnaydigan barcha bolalar soni: {len(barcha_bolalar)} ta")

# 9.

# text = "olma anor olma uzum anor olma"
# words = text.split()

# word_counts = {}
# for word in words:
#     word_counts[word] = word_counts.get(word, 0) + 1

# print(word_counts)