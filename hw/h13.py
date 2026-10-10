# class user:
#     def __init__(self, username, full_name, email):
#         self.username = username
#         self.full_name = full_name
#         self.email = email
#
#     def get_info(self):
#         return "Foydalanuvchi: {a}, ismi: {b}, email: {c}".format(a=self.username, b=self.full_name, c=self.email)
#
# user1 = user("Jam", "Alex Karp", "Alex123@gmail.com")
# print(user1.get_info())

# class phone:
#     def __init__(self, model, price, storage, ram, cpu):
#         self.model = model
#         self.price = price
#         self.storage = storage
#         self.ram = ram
#         self.cpu = cpu
#
#     def get_info(self):
#         return f"""Model: {self.model}
# Price: {self.price}
# Storage: {self.storage}
# RAM: {self.ram}
# CPU: {self.cpu}
# """
#
# phone1 = phone("Xiaomi", 10000000, 512, 16, "Snapdragon 8")
# print(phone1.get_info())


# 10 classes

# class laptop:
#     def __init__(self, brand, price, storage, ram, cpu, gpu):
#         self.brand = brand
#         self.price = price
#         self.storage = storage
#         self.ram = ram
#         self.cpu = cpu
#         self.gpu = gpu
#
#     def display(self):
#         return f"""Brand: {self.brand}
# Price: {self.price}
# Storage: {self.storage}
# RAM: {self.ram}
# CPU: {self.cpu}
# GPU: {self.gpu}
# """
#
# laptop1 = laptop("Lenovo", 1300, "1 TB", 32, "Intel", "RTX")
# print(laptop1.display())


# class OyinQahramoni:
#     def __init__(self, ism, kuch, jon=100):
#         self.ism = ism
#         self.kuch = kuch
#         self.jon = jon
#
#     def hujum(self, dushman):
#         dushman.jon -= self.kuch
#         if dushman.jon < 0:
#             dushman.jon = 0
#
#         print(f"{self.ism} {dushman.ism}ga hujum qildi! {dushman.ism} {self.kuch} jon yo'qotdi. "
#               f"({dushman.ism} qolgan jon: {dushman.jon})")
#
#     def davolan(self, shifo_miqdori):
#         self.jon += shifo_miqdori
#         if self.jon > 100:
#             self.jon = 100
#
#         print(f"{self.ism} davolandi (+{shifo_miqdori}). Joriy jon: {self.jon}")
#
#     def holat(self):
#         print(f"{self.ism} | Jon: {self.jon}/100 | Kuch: {self.kuch}")
#
# qahramon1 = OyinQahramoni(ism="Steve", kuch=20, jon=80)
# qahramon2 = OyinQahramoni(ism="Zombie", kuch=15, jon=100)
#
# print("--- O'YIN BOSHLANDI ---")
# qahramon1.holat()
# qahramon2.holat()
# print("-" * 25)
#
# qahramon1.hujum(qahramon2)
# qahramon2.hujum(qahramon1)
# print("-" * 25)
#
# qahramon1.davolan(50)
#
# qahramon1.holat()
# qahramon2.holat()