#This program runs the Collatz sequence
# If a number is even then it will be divided by 2
# If a number is odd, then it'll 3*number+1 and print




# Collatz Function
def collatz(number):

    try:
        number = int(number) #takes whatever is put into collatz function and attempts to convert to an integer
        while number > 1: #loops till original input is manipulated into 1
            if number % 2 == 0:  #checks to see if the number is even using remainders
                number = number/2
                print(number)
            else: #if number is odd, performs this function
                number = 3*number+1
                print(number)
    except ValueError: #if a string is entered into collatz, program stops and prints error message
            print('Error! Please enter a number! ')
            collatz(input('Please enter a number. ')) #reprompts the user to enter a number


#Main Task
collatz(input('Please enter a number. '))

