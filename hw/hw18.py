import json
import pickle
import time

class Sessiya:
    def __enter__(self):
        self.ism = input("Ismingizni kiriting: ")
        print(f"Xush kelibsiz, {self.ism}!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Xayr, {self.ism}!")
        if exc_type:
            print(f"[Xatolik ushlandi]: {exc_val}")
        return True


def task_2():
    with Sessiya():
        print("Sessiya davom etmoqda")
        x = 1 / 0

def task_3():
    try:
        print("A")
        x = 1 / 0
        print("B")
    except ZeroDivisionError:
        print("C")
    else:
        print("D")
    finally:
        print("E")
class Taymer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time


def bonus_task():
    data = {"users": [{"id": i, "name": f"User_{i}", "score": i * 1.5} for i in range(200000)]}

    with Taymer() as json_timer:
        with open("data.json", "w") as f:
            json.dump(data, f)

    with Taymer() as pickle_timer:
        with open("data.pkl", "wb") as f:
            pickle.dump(data, f)

    print(f"JSON saqlash vaqti:   {json_timer.elapsed_time:.5f} soniya")
    print(f"Pickle saqlash vaqti: {pickle_timer.elapsed_time:.5f} soniya")

    if pickle_timer.elapsed_time < json_timer.elapsed_time:
        print("Xulosa: Pickle tezroq ishladi!")
    else:
        print("Xulosa: JSON tezroq ishladi!")


task_2()
task_3()
bonus_task()