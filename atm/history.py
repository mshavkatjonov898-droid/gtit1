import constants

def history():
    if constants.history:
        for i in constants.history:
            print(i)
        print(f"Jami kirim: {constants.sum_discount} so'm ({constants.count_discount} ta)")
        print(f"Jami chiqim: {constants.sum_withdraw} so'm ({constants.count_withdraw} ta)")