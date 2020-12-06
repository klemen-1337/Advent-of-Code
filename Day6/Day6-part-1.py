file = open("input.txt")

groups = file.read().split("\n")
temp = ""
fin = []

for ele in groups:
    if ele != '':
        temp += ele
    else:
        fin.append(temp)
        temp = ""
fin.append(temp)

ct = 0
for group in fin:
    uniq = set(group)
    ct += len(uniq)
print(ct)
# 6809
