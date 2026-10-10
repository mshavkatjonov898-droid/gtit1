import math
import constants
import random

def get_money():
    try:
        a = int(input("Necha pul olasiz: "))
        if a < 0:
            raise ValueError("Xato: Summa musbat bo'lishi kerak!")
        if a % 5000 != 0:
            raise ValueError("Xato: Bankomat faqat 5000 lik kupyuralar beradi!")
        komissiya = math.ceil(a/100)

        if a + komissiya > constants.balance:
            print("Xato: Mablag' yetarli emas!")
            return
        b = random.randint(100000, 999999)
        constants.balance -= a + komissiya
        print(f"Oling: {a} so'm (komissiya: {komissiya} so'm)\n Chek raqami: №{b}\n Qoldiq: {constants.balance} so'm")
        constants.sum_withdraw += a
        constants.history.append(f"KIRIM: +{a} so'm")
        constants.count_withdraw += 1

    except ValueError as e:
        print(f"Xato: Son kiriting!{e}")