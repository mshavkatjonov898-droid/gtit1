import json

def jurnalga_yoz(matn):
    with open("jurnal.txt", "a") as f:
        f.write(f"[LOG] {matn}\n")

class Xona:
    __jami = 0

    def __init__(self, raqam, narx, sigim=2):
        self.raqam = raqam
        self.narx = narx
        self.sigim = sigim
        Xona.__jami +=1
        self.__band = False
        self.mehmon = None

    def bandmi(self):
        return self.__band

    def band_qil(self, mehmon):
        if self.__band:
            return False
        self.__band = True
        self.mehmon = mehmon
        return True

    def boshat(self):
        self.__band = False
        self.mehmon = None

    def turi(self):
        return "Oddiy"

    def __str__(self):
        if self.__band:
            holat = f"BAND ({self.mehmon.ism})"
        else:
            holat = "bo'sh"
        return f"{self.raqam}-xona | {self.turi()} | {self.narx} so'm | {self.sigim} kishi | {holat}"

    def __gt__(self, other):
        return self.narx > other.narx

class Lyuks(Xona):
    def __init__(self, raqam, narx, sigim=4, nonushta=True):
        super().__init__(raqam, narx, sigim)
        self.nonushta = nonushta

    def turi(self):
        return "Lyuks"

    def __str__(self):
        qoshimcha = "tekin noushta"
        return super().__str__() + qoshimcha

class Mehmon:
    def __init__(self, ism, telefon):
        self.ism = ism
        self.telefon = telefon

    def __str__(self):
        return f"{self.ism} ({self.telefon})"

class Mexmonxona:
    def __init__(self, nom):
        self.__xonalar = []
        self.nom = nom

    def __len__(self):
        return len(self.__xonalar)

    def __getitem__(self, i):
        return self.__xonalar[i]

    def __str__(self):
        return f"{self.nom}: {len(self)} ta xona"

    def xona_qosh(self, xona):
        self.__xonalar.append(xona)
        print(f"{xona.raqam}-xona qo'shildi ({xona.turi()})")
        jurnalga_yoz(f"{xona.raqam}-xona qo'shildi")

    def top(self, raqam):
        for x in self.__xonalar:
            if x.raqam == raqam:
                return x
        return None

    def joylash(self, raqam, mehmon):
        xona = self.top(raqam)
        if xona is None:
            print("Bunday xona yo'q!")
        elif not xona.band_qil(mehmon):
            print(f"{raqam}-xona allaqachon band!")
        else:
            print(f"{mehmon.ism} {raqam}-xonaga joylashdi")
            jurnalga_yoz(f"{mehmon.ism} {raqam}-xonaga joylashdi")

    def boshat(self, raqam):
        xona = self.top(raqam)
        if xona is None:
            print("Bunday xona yo'q!")
        elif not xona.bandmi():
            print("Bu xona allaqachon bo'sh")
        else:
            ism = xona.mehmon.ism
            xona.boshat()
            print(f"👋 {ism} {raqam}-xonadan chiqdi")
            jurnalga_yoz(f"{ism} {raqam}-xonadan chiqdi")

    def hammasi(self):
        print(self)
        if not self.__xonalar:
            print("   (xonalar yo'q)")
        for x in self.__xonalar:
            print("  ", x)

    def boshlar(self):
        return [x for x in self.__xonalar if not x.bandmi()]

    def eng_qimmat(self):
        if not self.__xonalar:
            return None
        return max(self.__xonalar)

    def daromad(self):
        return sum(x.narx for x in self.__xonalar if x.band_mi())

    def saqla(self, fayl="mehmonxona.json"):
        data = []
        for x in self.__xonalar:
            data.append({
                "raqam": x.raqam, "narx": x.narx, "sigim": x.sigim,
                "lyuks": isinstance(x, Lyuks),
                "mehmon": None if x.mehmon is None else [x.mehmon.ism, x.mehmon.telefon],
            })
        with open(fayl, "w") as f:
            json.dump(data, f, indent=2)
        print(f"💾 {len(data)} ta xona saqlandi {fayl}")
        jurnalga_yoz(f"{len(data)} ta xona saqlandi")

    @classmethod
    def yukla(cls, nom, fayl="mehmonxona.json"):
        m = cls(nom)
        try:
            with open(fayl, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("ℹ️ Saqlangan fayl topilmadi — bo'sh mehmonxona ochildi")
            return m
        for d in data:
            if d["lyuks"]:
                x = Lyuks(d["raqam"], d["narx"], d["sigim"])
            else:
                x = Xona(d["raqam"], d["narx"], d["sigim"])
            if d["mehmon"]:
                x.band_qil(Mehmon(*d["mehmon"]))
            m.xona_qosh(x)
        print(f"📂 {len(m)} ta xona yuklandi")
        jurnalga_yoz(f"{len(m)} ta xona fayldan yuklandi")
        return m


def main():
    m = Mexmonxona.yukla("Ustudy Hotel")
    while True:
        print("""
        === 🏨 MEHMONXONA ===
        1. Xona qo'shish
        2. Barcha xonalar
        3. Mehmon joylash
        4. Xonani bo'shatish
        5. Bo'sh xonalar
        6. Eng qimmat xona
        7. Bugungi daromad
        8. Saqlash
        9. Jurnalni ko'rish
        0. Chiqish""")
        tanlov = input("Tanlang: ").strip()
        try:
            if tanlov == "1":
                raqam = int(input("Xona raqami: "))
                if m.top(raqam):
                    print("Bu raqamli xona bor!")
                    continue
                narx = int(input("Narxi: "))
                turi = input("Turi (oddiy/lyuks) - ko'rsatilganidek yozing: ")
                if turi == "lyuks":
                    m.xona_qosh(Lyuks(raqam, narx))
                else:
                    m.xona_qosh(Xona(raqam, narx))
            elif tanlov == "2":
                m.hammasi()
            elif tanlov == "3":
                raqam = int(input("Xona raqami: "))
                ism = input("Mehmon ismi: ")
                tel = input("Telefon: ")
                m.joylash(raqam, Mehmon(ism, tel))
            elif tanlov == "4":
                m.boshat(int(input("Xona raqami: ")))
            elif tanlov == "5":
                bosh = m.boshlar()
                print(f"Bo'sh xonalar: {len(bosh)} ta")
                for x in bosh:
                    print("  ", x)
            elif tanlov == "6":
                x = m.eng_qimmat()
                if x:
                    print(x)
                else:
                    print("Xonalar yo'q")
            elif tanlov == "7":
                print(f"Bugungi daromad: {m.daromad()} so'm")
            elif tanlov == "8":
                m.saqla()
            elif tanlov == "9":
                try:
                    with open("jurnal.txt", "r") as f:
                        if f.read():
                            print(f.read())
                        else:
                            print("Jurnal bo'sh")
                except FileNotFoundError:
                    print("(jurnal yo'q")
            elif tanlov == "0":
                m.saqla()
                break
            else:
                print("Noto'g'ri tanlov")
        except ValueError:
            print("Son kiriting!")
        finally:
            print(f"xoanalar soni: {len(m)}")


main()