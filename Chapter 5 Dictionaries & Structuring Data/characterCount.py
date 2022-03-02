# This program counts how many times a certain character appears in a message

# Pretty Print character count (sorts kyes in a nicer list)

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0) #sets default character amount in dictionary count to 0
    count[character] = count [character] + 1
pprint.pprint(count)
#printing pretty tet as a string
print(pprint.pformat(count))
