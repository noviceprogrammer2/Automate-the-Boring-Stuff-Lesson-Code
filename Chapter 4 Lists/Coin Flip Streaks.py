#Program finds percentage of how many times six heads or six tails comes up in a randomly gneerated list

import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinflips = []
    for i in range(0,100):
        coinvalue = [random.randint(0,1)];  #0 equal to tails 1 equal to heads
        coinflips.append(coinvalue)
    print(coinflips)


    # Code that checks if there is a streak of 6 heads or tails in a row.'

    for i in range(len(coinflips)):
        if coinflips[i] == coinflips[i-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks=numberOfStreaks+1

print('Chance of streak: %s%%' % (numberOfStreaks / (10000)))
