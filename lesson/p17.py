try:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())  # .strip() removes the trailing '\n'
except FileNotFoundError:
    print("asdfghjkl")