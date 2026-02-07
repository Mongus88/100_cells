cells_number = 100
cells = ["close"] * cells_number
opened = (0)

for i in range(1,cells_number + 1):
    for j in range(i - 1,cells_number,i):
        if cells[j] == "close":
            cells[j] = "open"
        else:
            cells[j] = "close"

for k in cells:
    if k == "open":
        opened += 1

print(f"Opened cells: {opened}")
