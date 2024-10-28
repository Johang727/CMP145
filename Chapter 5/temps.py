with open('temps.txt', 'r') as text:
    highest = 'n'
    for i in text:
        if highest == 'n':
            highest = int(i)
        else:
            if int(i) > highest:
                highest = int(i)
    print(highest)