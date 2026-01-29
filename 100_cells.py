cells_number = 100
cells = ["close"] * cells_number

for i in range(1,cells_number + 1):
    for j in range(i - 1,cells_number,i):
        if cells[j] == "close":
            cells[j] = "open"
        else:
            cells[j] = "close"
for index, state in enumerate(cells):
    print(f"{index + 1}. door: {state}")
