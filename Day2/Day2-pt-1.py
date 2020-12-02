file  = open("input.txt")

ct = 0;

for line in file:

    len, char, password = line.split()
    len_from, len_to = map(int, len.split("-"))

    char = char[0]

    valid = 0

    for ch in password:
        if (ch == char):
            valid+=1

    if(valid >= len_from) and (valid <= len_to):
        ct+=1

print(ct)
