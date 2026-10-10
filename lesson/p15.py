class Hayvon:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def ovoz(self):
        pass

class It(Hayvon):
    def __init__(self, ism, yosh, jon=100):
        super().__init__(ism, yosh)
        self.__jon = jon

    def jon_holati(self):
        return f"Itning jon holati: {self.__jon}"

    def ovqatlantir(self):
        if self.__jon >= 100:
            print(f"Jon holati {self.__jon} shuning uchun ortiqcha jon qo'shish mumkin emas!")
        return self.__jon + 10

    def ovoz(self):
        return "It ovozi"

class Qush(Hayvon):
    def __init__(self, ism, yosh, jon=100):
        super().__init__(ism, yosh)
        self.__jon = jon

    def jon_holati(self):
        return f"Qushning jon holati: {self.__jon}"

    def ovqatlantir(self):
        if self.__jon >= 100:
            print(f"Jon holati {self.__jon} shuning uchun ortiqcha jon qo'shish mumkin emas!")
        return self.__jon + 10

    def ovoz(self):
        return "Qush ovozi"


hayvonlar = [It("a", 14, 100), Qush("b", 15, 100)]
for hayvon in hayvonlar:
    print(hayvon.ovoz())