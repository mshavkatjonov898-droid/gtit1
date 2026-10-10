info = 0
warning = 0
error = 0

with open("jurnal.log", "r", encoding="utf-8") as f:
    for line in f:
        if " INFO " in line:
            info += 1
        if " WARNING " in line:
            warning += 1
        if " ERROR " in line:
            error += 1

print(f"INFO: {info}")
print(f"WARNING: {warning}")
print(f"ERROR: {error}")
