#Program checks if input is a strong password

#Password Requirements
# at least 8 characters long
# Contains upper case and lower case letters and at least one digit



import re


def passwordrequirements(phrase):

    if len(password) < 8:
        print('Error! Password less than 8 characters.')
        return


    uppercase_regex = re.compile(r'[A-Z]')
    listofUppercase = uppercase_regex.findall(phrase)

    lowercase_regex = re.compile(r'[a-z]')
    listofLowercase = lowercase_regex.findall(phrase)

    digit_regex = re.compile(r'[0-9]')
    listofDigit = digit_regex.findall(phrase)

    if len(listofUppercase) == 0 or len(listofLowercase) == 0 or len(listofDigit) == 0:
        print('Error! Password isn\'t Valid. Please enter a password that is at least 8 characters and contains one upper case, one lower case, and one number')
    else:
        print('Password: %s is valid!' %(phrase))


password = ''

passwordrequirements(password)
