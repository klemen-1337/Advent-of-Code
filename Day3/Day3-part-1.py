f= open("input.txt")
file = [x for x in f.read().split("\n")[::1]]

ct = 0
ind = 0

for line in file:
    if(line[ind % len(file[0])] == "#"):
        ct+=1

    ind += 3

print(ct)

# result = 187


