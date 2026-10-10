# for i in range(1, 31):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)
#     elif i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0 and i % 5 != 0:
#         print("Fizz")
#     elif i % 3 != 0 and i % 5 == 0:
#         print("Buzz")

a = int(input())
for j in range(1):
    for i in range(1, a + 1):
        print(" " * (a-i) + "*" * (2*i-1))
        b = len(" " * (a-i) + "*" * (2*i-1))
    print(" " * int(b/2) + "|")