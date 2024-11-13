#vtrs = []
vtrs = {}

with open('voters.txt', 'r') as vtr_txt:
    votes = [0] * 10
    for lines in vtr_txt:
        data = lines.split(',') # ID, v1, v2, v3
        if data[0] not in vtrs:
            # allow
            #vtrs.append(data[0])
            vtrs[data[0]] = 'dummy'
            votes[int(data[1])] +=1
            votes[int(data[2])] +=1
            votes[int(data[3])] +=1

print(votes)



# sort using dictionary, {band:votes}