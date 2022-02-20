from random import randint

with open("a.txt", "w") as file:
    for i in range(25):
        file.write(f"{randint(0, 100)}\n")

data = []
with open("a.txt", "r") as file:
    for line in file.readlines():
        data.append(line)

print(data)
