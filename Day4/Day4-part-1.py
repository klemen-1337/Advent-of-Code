f = open("input.txt")

valid = 0

file = f.read().split("\n\n")
for line in file:
    line = line.replace("\n" ," ")
    print(line)
    d = dict(x.split(":") for x in line.split(" "))

    if (len(d.keys()) == 8):
        valid += 1

    if(not d.keys().__contains__("cid")):
        if (len(d.keys()) == 7):
            valid += 1

print(valid)

