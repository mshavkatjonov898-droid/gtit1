import constants
import pul_yechish
import discount
import history

def main():
    attempt = 0
    while attempt < 3:
        attempt += 1
        try:
            pin1 = int(input("PIN kodni kiriting: "))
            if pin1 == constants.pin_code:
                print("Xush kelibsiz, Ustudy Bank!")
                while True:
                    tanlov = input("""===== USTUDY BANK =====
1. Balansni ko'rish
2. Pul olish
3. Pul qo'yish
4. Tarix
0. Chiqish
Tanlang: """)
                    if tanlov == "1":
                        print(f"Your balance is {constants.balance}.")
                    elif tanlov == "2":
                        pul_yechish.get_money()
                    elif tanlov == "3":
                        discount.discount_money()
                    elif tanlov == "4":
                        history.history()
                    elif tanlov == "0":
                        break
                    else:
                        print("Bunday bo'lim yo'q!")
        except ValueError:
            print(f"Noto'g'ri PIN, urinishlar qoldi: {attempt}")
        else:
            print(f"Xato: PIN noto'g'ri! Qolgan urinishlar: {attempt}")
        if attempt == 3:
            print("Karta bloklandi! Bankka murojaat qiling.")
            break
main()