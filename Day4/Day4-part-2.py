import re
f = open("input.txt")
pattern = re.compile("^#[a-z0-9]{6}")
ecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def validation(d):
    v = 0
    for key, value in d.items():
        if(key == "byr"):
            v += int(value) >= 1920 and int(value) <= 2002
        if (key == "iyr"):
            v += int(value) >= 2010 and int(value) <= 2020
        if (key == "eyr"):
            v += int(value) >= 2020 and int(value) <= 2030
        if (key == "hgt"):
            if("in" in value):
                value = int(value.replace("in", ""))
                v += value >= 59 and value <= 76
            if("cm" in str(value)):
                value = int(value.replace("cm", ""))
                v += value >= 150 and value <= value
        if (key == "hcl"):
             if(pattern.fullmatch(value)):
                 v+=1

        if (key == "ecl"):
            v += value in ecl
        if (key == "pid"):
            v += len(value) == 9 and value.isdigit()
        if (key == "cid"):
            v += 1

    return v == len(d.keys())


valid = 0

file = f.read().split("\n\n")
for line in file:
    line = line.replace("\n" ," ")
    d = dict(x.split(":") for x in line.split(" "))

    if (len(d.keys()) == 8):
        if(validation(d)):
            valid += 1

    if(not d.keys().__contains__("cid")):
        if (len(d.keys()) == 7):
            if(validation(d)):
                valid += 1

print(valid)

