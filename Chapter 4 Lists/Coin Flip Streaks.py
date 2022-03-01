#Program finds percentage of how many times six heads or six tails comes up in a randomly gneerated list

import random
numberOfStreaks = 0
streak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinflips = []
    for i in range(0,100):
        coinvalue = [random.randint(0,1)];  #0 equal to tails 1 equal to heads
        coinflips.append(coinvalue)
    print(coinflips)


    # Code that checks if there is a streak of 6 heads or tails in a row.'

    for i in range(len(coinflips)): #for counter in range of the length of coinflips (100)
        if coinflips[i] == coinflips[i-1]: #if the number at that spot is equal to the number before it in the list, streak +1
            streak = streak +  1
        else:
            streak = 0 #no repeat sets streak back to 0
        if streak == 6: #if streak equals 6, than number of streaks += 1
            numberOfStreaks=numberOfStreaks+1

print('Chance of streak: %s%%' % (numberOfStreaks / (10000)))
