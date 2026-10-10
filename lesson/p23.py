def ikki_marta(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        result2 = func(*args, **kwargs)
        return f"{result}\n{result2}"
    return wrapper


@ikki_marta
def salom_ber(name):
    return f'salom {name}'


print(salom_ber('ALi'))


# import time
# def taymer(func):
#     def wrapper(*args,**kwargs):
#         d = time.time()
#         result = func(*args,**kwargs)
#         t = time.time()
#
#         return f"{t-d:.2f}"
#     return wrapper
#
# # @montiring
# # def fo():
# #     pass
# #
# # fo()
#
#
#
# @taymer
# def sekin_funksiya():
#     for i in range(10_0000):
#         print(i)
#
# print(sekin_funksiya())