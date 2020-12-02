f = open("input.txt", "r")

text = []


for line in f:
    text.append(line)

for num in text:
    number = int(num)
    for num2 in text:
        number2 = int(num2)
        if(number+number2 == 2020):
            print(number*number2)
            break
    else:
        continue
    break

