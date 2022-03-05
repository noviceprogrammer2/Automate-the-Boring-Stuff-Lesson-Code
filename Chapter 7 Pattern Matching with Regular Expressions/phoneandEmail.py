
# in Python 3
# Program extracts phone number and emails from text, then prints in neatly formatted string

import pyperclip, re # imports pyperclip for copying and pasting strings, imports re for pattern finding

# Creating Phone Regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits 
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension  
    )''', re.VERBOSE)

# Email Regex

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

# TODO: Find Matches in clipboard text.

# TODO: Copy Results to the clipboard.
