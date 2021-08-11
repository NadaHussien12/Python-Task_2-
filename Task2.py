# N_Letter #
row = 5
for i in range(row):
    for j in range(row):
        if j == 0 or j == row-1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

# A_Letter #
row = 5
col = (row//2)
for i in range(row):
    for j in range(col+1):
        if ((j == 0 or j == col) and i != 0) or ((i == 0 or i == col) and (j != col and j != 0)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

# D_Letter #
row = 5
for i in range(row):
    for j in range(row):
        if j == 0 or ((j == row-1) and (i != 0 and i != row-1)) or ((i == 0 or i == row-1) and (j != 0 and j != row-1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

# A_Letter #
row = 5
col = (row//2)
for i in range(row):
    for j in range(col+1):
        if ((j == 0 or j == col) and i != 0) or ((i == 0 or i == col) and (j != col and j != 0)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    