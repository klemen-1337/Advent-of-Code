file = open("input.txt")

groups = file.read().split("\n")
temp = ""
fin = []

for ele in groups:
    if ele != '':
        temp += ele + " "
    else:
        temp = temp[:-1]
        fin.append(temp)
        temp = ""
fin.append(temp)

ct = 0
for group in fin:
    uniq = {x for x in group if x != " "}
    for q in uniq:
        ct += group.count(q) == len(group.split(" "))

print(ct)
# 3394

