# Expression that can detect dates in the DD/MM/YYYY format to the year 9999

#Date Info

#April, June, September, November have 30 days
# February has 28 Days
# Rest of months have 31 days

import re

#TODO Create expression that detects dates first (REGEX)
def isvalidDate(testdate):

    dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})') #dateRegex expression that looks for date format makes groups

    day = []
    month = []
    year = []
    for groups in dateRegex.findall(testdate):
        day.append(groups[0])
        month.append(groups[1])
        year.append(groups[2])
    #prints list of days, months, and years
    validdays_int_10_31 = list(range(10,32)) #creates valid day values for 10 through 31
    validdays_str_10_31 = list(map(str,validdays_int_10_31)) #changes days from 10-31 in integers to strings
    validdays_str_01_09 = ['01','02','03','04','05','06','07','08','09']
    validdays_str = validdays_str_01_09 + validdays_str_10_31 #creates total string that has every actual date

    #Checks day values to see if they're at least a day value between 01 and 31, if not, removes date from list
    i = 0
    while i < len(day):
        if day[i] not in validdays_str:
                #removes day, month, and year from list at same position
                day.remove(day[i])
                month.remove(month[i])
                year.remove(year[i])
        else:
            i = i + 1








    # Checking months of april, june, september, & november for proper days
    m = 0
    while m < len(month):
        if month[m] == '04' or '06' or '09' or '11': #if months are april, june, september, or november
            if day[m] == '31':
                 #removes day, month, and year from list at same position
                day.remove(day[m])
                month.remove(month[m])
                year.remove(year[m])
        elif month[m] == '02': #if month is february, and days are greater than 28, remove incorrect date from list
            if day[m] == '29' or '30' or '31':
                day.remove(day[m])
                month.remove(month[m])
                year.remove(year[m])
        else:
            m=m+1

    #Dealing with remaining valid dates

    for valid in range(len(year)): #print statement that iterates over the remaining valid dates and prints them
        print('Date Found: %s/%s/%s' % (str(day[valid]), str(month[valid]), str(year[valid])))






    # Checking days (valid string days can be from 01-31)







#TODO create expression that then checks stored date to see if it's a valid date



test_dates = ('Anus farts on 31/05/2001 and gwen is born on 08/09/2003. ')
isvalidDate(test_dates)
