f = open("input.txt")

maxId=0

for line in f:

    seats = range(128)
    column = range(8)

    for char in line:

        if (char == "F"):
            seats = seats[:len(seats)//2]
        elif (char == "B"):
            seats = seats[len(seats)//2:]
        elif (char == "L"):
            column = column[:len(column)//2]
        elif (char == "R"):
            column = column[len(column)//2:]

    ID = seats[0] * 8 + column[0]
    if(ID > maxId):
        maxId = ID

print(maxId)    # 848
