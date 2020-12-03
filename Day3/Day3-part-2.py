f= open("input.txt")
file = [x for x in f.read().split("\n")[::2]]   # 1,1,1,1,2

ct = 0
ind = 0

for line in file:
    if(line[ind % len(file[0])] == "#"):
        ct+=1

    ind += 1                                    # 1,3,5,7,1

print(ct)


# result = 86*187*75*89*44 = 4723283400

