#Program checks to see if string is an American Phone Number

def isPhoneNumber(text):
    if len(text) !=12: #if length of string is not 12, returns false
        return False
    for i in range(0,3): #for string 0-2 if string at that value is not a decimal, return false
        if not text[i].isdecimal():
            return False
    if text[7] != '-': #if at text[7] is not a hyphen, return false
        return False
    for i in range(8,12): #checks last four characters of string to make sure they are numbers, returns false if not
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
#for character in the total length of message
for i in range(len(message)):
    chunk = message[i:i+12] #examines chunk of 12 (same length as phone number)
    if isPhoneNumber(chunk): #if that chunk is a phone number, it returns the message with the phone number found
        print('Phone number found: ' + chunk)
print('Done')
