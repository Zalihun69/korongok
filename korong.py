
board = [[0 for _ in range(8)] for _ in range(8)]  

def print_board():
    print("\nTábla:")
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

print("Korongok elhelyezése a táblán (1-től 8-ig számozva).")
print("Hagyja üresen a sort, hogy kilépjen.")

while True:

    row_input = input("Adja meg a korong sorát (1-8): ").strip()
    if row_input == "":
        break

    col_input = input("Adja meg a korong oszlopát (1-8): ").strip()
    if col_input == "":
        break

    if not (row_input.isdigit() and col_input.isdigit()):
        print("Hibás bemenet! Csak számokat adjon meg.")
        continue

    row = int(row_input)
    col = int(col_input)

    if 1 <= row <= 8 and 1 <= col <= 8:
        if board[row-1][col-1] == 0:
            board[row-1][col-1] = 1
            print("Korong elhelyezve.")
        else:
            print("Ez a mező már foglalt!")
    else:
        print("Hibás bemenet! A számoknak 1 és 8 között kell lenniük.")

    print_board()

print("A játék véget ért. Végső táblaállás:")
print_board()
