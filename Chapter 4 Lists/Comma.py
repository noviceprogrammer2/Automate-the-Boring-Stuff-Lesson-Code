
#Enter any list when calling the comma function
#Program will add commas after each word before the last and an and before the last word
#EX: comma['apples','bananas','oranges'] outputs 'apples, bananas, and oranges'

def comma(words):
    words = list(words)
    length = len(words)
    commaamount = length - 1 #calculates number of commas needed
    try:
    #inserts , after each word excluding last word
        for i in range(commaamount):
            words[i] = words[i] + ', '
        #inserts and after the last comma
        words[i] = words[i] + 'and '
        #joins words together (joins the list which turns into a string after .join)
        sentence = ''.join(words)
        print(sentence)
    #if a blank list is entered, unbound error is replaced with this message
    except UnboundLocalError:
        print('Error! No list of words entered! Please try again')




comma(['apples','bananas','oranges'])
