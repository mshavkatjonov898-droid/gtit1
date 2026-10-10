ombor = {}


def add_product():
    p_name = input("Mahsulot nomi: ").strip()
    if p_name in ombor:
        print(f"'{p_name}' allaqachon bor! Yangilash bo'limidan foydalaning.")
        return
    price = int(input("Narxi (so'm): "))
    amount = int(input("Soni (dona): "))
    ombor[p_name] = {"narxi": price, "soni": amount}
    print(f"'{p_name}' omborga qo'shildi!")


def search():
    product = input("Qaysi mahsulotni qidiramiz?: ")
    for name, info in ombor.items():
        if product == name:
            print(f"{name}: omborda {info['soni']} dona, {info['narxi']} so'm")
        else:
            print("asd")

def modify_ombor():
    product = input("Qaysi mahsulotni yangilaymiz?:")
    if product not in ombor:
        print(product, "omborda yo'q.")
        return
    else:
        choice = input("""1 — Kirim (soni oshadi)
2 — Chiqim (soni kamayadi)
3 — Yangi narx: """)
        if choice == "1":
            kirim = int(input("Nechta keldi?: "))
            ombor[product]["soni"] = ombor[product]["soni"] + kirim
            print(f"✅ Kirim qabul qilindi. Endi {[product]}: {ombor[product]["soni"]} dona")
        elif choice == "2":
            chiqim = int(input("Nechta chiqdi?: "))
            if chiqim > ombor[product]["soni"]:
                print("Chiqim ombordagi mahsulotdan ko'p, chiqimni kamaytiring!")
                return
            ombor[product]["soni"] = ombor[product]["soni"] - chiqim
            print(f"✅ Chiqim qabul qilindi. Endi {[product]}: {ombor[product]["soni"]} dona")
        elif choice == "3":
            new_price = int(input("Yangi narx: "))
            ombor[product]["narxi"] = new_price
            print(f"✅ {[product]} narxi yangilandi: {new_price} so'm")


def delete():
    product = input("Qaysi mahsulotni o'chiramiz?: ")
    check = input(f"{product} rostdan o'chirilsinmi? (ha/yoq): ").lower()
    if check == "ha":
        ombor.pop(product)
        print(f"🗑️ {product} ombordan o'chirildi.")
    elif check == "yoq":
        print("Bekor qilindi.")


def all1():
    for name, info in ombor.items():
        print(f"💰 Ombordagi jami boylik: {info["narxi"] * info["soni"]} so'm")

def main():
    print("""========================================
   📦 OMBORXONA TIZIMI v1.0
========================================""")
    while True:
        choice = input("""
1 — Mahsulot qo'shish
2 — Barcha mahsulotlar
3 — Qidirish
4 — Yangilash (kirim/chiqim/narx)
5 — O'chirish
6 — Umumiy qiymat
0 — Chiqish
>>> Bo'limni tanlang: """)
        if choice == "1":
            add_product()
        elif choice == "2":
            if not ombor:
                print("Ombor hozircha bo'sh.")
            else:
                print("--- OMBORDAGI MAHSULOTLAR ---")
                print("""----------------------------------------
MAHSULOT              NARXI    SONI
----------------------------------------""")
                for name, info in ombor.items():
                    print(f"{name}                 {info['narxi']}      {info['soni']}")
        elif choice == "3":
            search()
        elif choice == "4":
            modify_ombor()
        elif choice == "5":
            delete()
        elif choice == "6":
            all1()
        elif choice == "0":
            print("Dastur tugadi. Xayr!")
            break
        else:
            print("0-6 oralig'ida tanlang!")

main()