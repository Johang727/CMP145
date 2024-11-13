import random
num = int(input())


with open('voter.txt', 'w') as vtr_txt:
    for i in range(num):
        id_1 = random.randint(00, 99)
        id_2 = random.randint(00000, 99999)
        v1 = random.randint(0, 9)
        v2 = random.randint(0, 9)
        v3 = random.randint(0, 9)
        
        vtr_txt.write(f"{id_1:02}-{id_2:05},{v1},{v2},{v3}\n")

