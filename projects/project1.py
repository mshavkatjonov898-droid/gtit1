kutubxona = {}


def add_book():
    b_name = input("Kitob nomi: ")
    if b_name in kutubxona:
        print(f"'{b_name}' allaqachon bor! Yangilash bo'limidan foydalaning.")
        return
    author = input("Muallifi: ")
    amount = int(input("Nechta nusxa: "))
    kutubxona[b_name] = {"muallif": author, "soni": amount, "ijarada": []}
    print(f"'{b_name}' kutubxonaga qo'shildi!")


def search_book():
    product = input("Qaysi kitobni qidiramiz?: ")
    if product in kutubxona:
        info = kutubxona[product]
        print(
            f"{product} | Muallif: {info['muallif']} | Mavjud: {info['soni']} dona | Ijarada: {len(info['ijarada'])} ta")
    else:
        print(f"{product} kutubxonada topilmadi.")


def rent_book():
    product = input("Qaysi kitobni ijaraga beramiz?: ")
    if product not in kutubxona:
        print(f"{product} kutubxonada topilmadi.")
    elif kutubxona[product]["soni"] <= 0:
        print(f"Kechirasiz, '{product}' kitobidan boshqa qolmadi (barchasi ijarada).")
    else:
        who = input("Kimga berilyapti?: ")
        kutubxona[product]["soni"] -= 1
        kutubxona[product]["ijarada"].append(who)
        print(f"'{product}' {who}ga berildi. Qoldi: {kutubxona[product]['soni']} ta")


def give_back():
    claiming_b = input("Qaysi kitob qaytarilyapti?: ")
    if claiming_b not in kutubxona:
        print(f"{claiming_b} kutubxonada topilmadi.")
    else:
        who1 = input("Kim qaytaryapti?: ")
        if who1 not in kutubxona[claiming_b]["ijarada"]:
            print(f"{who1} bu kitobni olmagan edi!")
        else:
            kutubxona[claiming_b]["ijarada"].remove(who1)
            kutubxona[claiming_b]["soni"] += 1
            print(f"{claiming_b} qaytarildi. Rahmat, {who1}!")


def debt():
    print("--- Qarzdorlar ro'yxati ---")
    qarz_bor = False
    for name, info in kutubxona.items():
        if info["ijarada"]:
            print(f"Kitob: {name} | Ijarachilar: {', '.join(info['ijarada'])}")
            qarz_bor = True

    if not qarz_bor:
        print("Hech kimda ijaradagi kitoblar yo'q.")


def delete():
    del_book = input("Qaysi kitob o'chiriladi?: ")
    if del_book not in kutubxona:
        print(f"{del_book} kutubxonada topilmadi.")
    else:
        check = input(f"{del_book} rostdan o'chirilsinmi? (ha/yoq): ").lower()
        if check == "ha":
            kutubxona.pop(del_book)
            print(f"{del_book} o'chirildi.")
        elif check == "yoq":
            print("Bekor qilindi.")
        else:
            print("Noto'g'ri buyruq kiritildi.")


def main():
    print("""============================================
   📚 KUTUBXONA TIZIMI v1.0
============================================""")
    while True:
        choice = input("""
1 — Kitob qo'shish
2 — Barcha kitoblar
3 — Qidirish
4 — Ijaraga berish
5 — Qaytarib olish
6 — Qarzdorlar ro'yxati
7 — Kitobni o'chirish
0 — Chiqish
>>> Bo'limni tanlang: """)

        if choice == "1":
            add_book()
        elif choice == "2":
            if kutubxona:
                print("Kutubxona hozircha bo'sh.")
            else:
                print("""----------------------------------------------------
KITOB              MUALLIF         MAVJUD   IJARADA
----------------------------------------------------""")
                for name, info in kutubxona.items():
                    print(f"{name} | {info['muallif']} | {info['soni']} | {info['ijarada']}")
                print(f"Jami: {len(kutubxona)} xil kitob")
        elif choice == "3":
            search_book()
        elif choice == "4":
            rent_book()
        elif choice == "5":
            give_back()
        elif choice == "6":
            debt()
        elif choice == "7":
            delete()
        elif choice == "0":
            print("Dastur tugadi. Kitob o'qishni unutmang!")
            break
        else:
            print("Bunday bo'lim yo'q. Qaytadan tanlang.")

main()