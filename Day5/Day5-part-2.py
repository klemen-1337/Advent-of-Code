f = open("input.txt")

idList = set()

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

    idList.add(seats[0] * 8 + column[0])

for i in range(min(idList), max(idList)):
    if(i not in idList):
        print(i)    # 682


