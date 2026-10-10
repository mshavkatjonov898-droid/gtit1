import constants

def discount_money():
    try:
        son = int(input("NEcha pul qoyasiz? "))
        if son < 0:
            raise ValueError("Xato: Summa musbat bo'lishi kerak!")
        else:
            constants.balance += son
            print(f"Qabul qilindi: {son} so'm \n Yangi balans: {constants.balance} so'm")
            constants.sum_discount += son
            constants.history.append(f"CHIQIM: -{son} so'm")
            constants.count_discount += 1
    except ValueError as e:
        print(f"Xato: Son kiriting! {e}")