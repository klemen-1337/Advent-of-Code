file  = open("input.txt")

ct = 0;

for line in file:

    len, char, password = line.split()
    len_from, len_to = map(int, len.split("-"))

    char = char[0]

    valid = 0

    if(password[len_from-1] == char) and (password[len_to-1] != char):
        valid+=1
    if(password[len_from-1] != char) and (password[len_to-1] == char):
        valid+=1

    if(valid == 1):
        ct += 1

print(ct)
