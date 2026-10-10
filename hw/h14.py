class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh  =yosh

    def tanishtir(self):
        pass

class Oqituvchi(Inson):
    def __init__(self, ism, yosh, fan):
        super().__init__(ism, yosh)
        self.fan = fan

    def tanishtir(self):
        return f"""==O'qituvchi==
Ism: {self.ism}
Yosh: {self.yosh}
Fan: {self.fan}
"""

class Oquvchi(Inson):
    def __init__(self, ism, yosh):
        super().__init__(ism, yosh)
        self.__baholar = []

    def baho(self, b:int):
        if 1 <= b <= 5:
            self.__baholar.append(b)
        else:
            print(f"Xato baho kiritildi! Baho 1 dab 5 gacha bo'lishi kerak!")

    def ortacha(self):
        if not self.__baholar:
            return 0
        return sum(self.__baholar) / len(self.__baholar)

    def tanishtir(self):
        return f"""==O'quvchi==
Ism: {self.ism}
Yosh: {self.yosh}
Baho: {self.ortacha()}
"""

class Direktor(Oqituvchi):
    def __init__(self, ism, yosh, fan, maktab_raqami):
        super().__init__(ism, yosh, fan)
        self.mr = maktab_raqami

    def tanishtir(self):
        return f"""==Direktor==
Ism: {self.ism}
Yosh: {self.yosh}
Maktab raqami: {self.mr}"""

d1 = Direktor("Akmal", 45, "math", 281)
o1 = Oqituvchi("Vali", 39, "math")
o2 = Oquvchi("Ozod", 16)

o2.baho(4)
o2.baho(3)
o2.baho(5)

odamlar_royxati = [o1, o2, d1]

print("\n--- Natijalar ---")
for odam in odamlar_royxati:
    print(odam.tanishtir())