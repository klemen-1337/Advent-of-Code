f = open("input.txt", "r")

text = []


for line in f:
    text.append(line)

for num in text:
    number = int(num)
    for num2 in text:
        number2 = int(num2)
        for num3 in text:
            number3 = int(num3)
            if(number + number2+number3 == 2020):
                print(number*number2*number3)
                break
        else:
            continue
        break
    else:
        continue
    break