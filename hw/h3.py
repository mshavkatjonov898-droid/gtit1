# # 1-vazifa

# names = ["John", "Alice", "Bob", "Mary", "David"]

# def messages(names):
#     for name in names:
#         print(f"Salom, {name}! Sizni ko'rishdan xursandman.")

# messages(names)

# # 2-vazifa

# nums = [-1, 2, 3.2, -4, 5.4]

# nums[0], nums[3] = nums[3], nums[0]

# nums[1] = 8

# # 3-vazifa

# t_shaxslar = ["Imom Buxoriy", "Alisher Navoiy", "Abu Rayhon Beruniy", "Ibn Sino", "Al-Xorazmiy"]

# z_shaxslar = ["Shavkat Mirziyoyev", "Abdulla Qodiriy", "Erkin Vohidov", "Muhammad Yusuf", "Hamid Olimjon"]

# a = t_shaxslar.pop(0)
# b = z_shaxslar.pop(0)

# print(f"Men tarixiy shaxslardan {a} bilan, zamonaviy shaxslardan esa {b} bilan suhbat qilishni istar edim")

# # 4-vazifa

# friends = ["Ali", "Vali", "Hasan", "Husan", "Olim"]

# friends.append("Sardor")
# friends.append("Diyor")

# friends.remove("Hasan")
# friends.insert(2, "Shahzod")
# friends.insert(0, "Komil")

# guests = friends[:]

# # 5-vazifa

# countries = ["USA", "Canada", "Germany", "France", "Italy"]

# print(len(countries))
# print(sorted(countries))
# print(sorted(countries, reverse=True))
# countries.sort(False)
# countries.sort(True)
# print(countries)

# # 6-vazifa

# juft_sonlar = list(range(120, 1201, 2))

# yigindi = sum(juft_sonlar)
# print("Sonlar yig'indisi:", yigindi)

# ayirma = max(juft_sonlar) - min(juft_sonlar)
# print("Eng katta va eng kichik son ayirmasi:", ayirma)

# elementlar_soni = len(juft_sonlar)
# print("Elementlar soni:", elementlar_soni)

# print("\nBoshidan 20 ta element:")
# print(juft_sonlar[:20])

# ortasi = elementlar_soni // 2
# print("\nO'rtasidan 20 ta element:")
# print(juft_sonlar[ortasi-10 : ortasi+10])

# print("\nOxiridan 20 ta element:")
# print(juft_sonlar[-20:])

# # 7-vazifa

# meals = ["Osh", "Manti", "Shashlik", "Lag'mon", "Somsa"]

# breakfast = meals[:]

# breakfast.remove("Shashlik")
# breakfast.remove("Lag'mon")

# breakfast.append("Non va choy")

# print(meals)
# print(breakfast)

# breakfast.tuple()

# breakfast[0] = "Non va qahva"

# Error: 'tuple' object does not support item assignment

# # 8-vazifa

# ballar = [78, 92, 45, 92, 88, 61, 92, 55]

# max_ball = max(ballar)
# min_ball = min(ballar)

# sum_ball = sum(ballar)

# print(ballar.count(max_ball))
# print(ballar.index(max_ball))

# # 9-vazifa

# a_class = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# b_class = ["Sardor", "Diyor", "Shahzod", "Komil", "Jasur"]

# katta_sinf = a_class + b_class

# print(sorted(katta_sinf))
# print(sorted(a_class))
# print(sorted(b_class))

# # 10-vazifa

# navbat = ["Aziz", "Malika", "Bobur"]

# mijoz1 = navbat.pop(0)

# print(f"{mijoz1} ketdi, xizmat ko'rsatildi.")

# navbat.insert(0, "Sardor")

# mijoz2 = navbat.pop(0)

# print(f"{mijoz2} ketdi, xizmat ko'rsatildi.")

# mijoz3 = navbat.pop(0)

# print(f"{mijoz3} ketdi, xizmat ko'rsatildi.")

# mijoz4 = navbat.pop(0)

# print(f"{mijoz4} ketdi, xizmat ko'rsatildi.")

# # 11-vazifa

# sonlar = [1, 3, 5, 3, 1]

# sonlar1 = sonlar.reverse()

# polindrom = sonlar == sonlar1

# print(f"Sonlar ro'yxati polindrommi? {polindrom}")

# # 12-vazifa

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX