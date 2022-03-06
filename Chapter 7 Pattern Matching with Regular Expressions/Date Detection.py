# Expression that can detect dates in the DD/MM/YYYY format to the year 9999

#Date Info

#April, June, September, November have 30 days
# February has 28 Days
# Rest of months have 31 days

import re

#Valid date function tests date to see if it's a valid date, if date is valid it prints it.
def isvalidDate(testdate):

    dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})') #dateRegex expression that looks for date format makes groups
    #creating an empty list of days, months, and years
    day = []
    month = []
    year = []
    for groups in dateRegex.findall(testdate): #for any matched dates
        day.append(groups[0]) #adds day to the day list
        month.append(groups[1]) #adds month to the month list
        year.append(groups[2]) #adds year to the year list

    #Below four lines of code create ranges of valid days


    validdays_int_10_31 = list(range(10,32)) #creates valid day integer values for 10 through 31
    validdays_str_10_31 = list(map(str,validdays_int_10_31)) #changes integers from 10-31 to strings
    validdays_str_01_09 = ['01','02','03','04','05','06','07','08','09'] #creates string list of valid days between 01-09
    validdays_str = validdays_str_01_09 + validdays_str_10_31 #creates total string that has every actual date from 01-31

    #Initial first test
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

    #Further Day checking
    # Checking months of april, june, september, & november for proper days
    m = 0
    while m < len(month): #while month is less than the length of months (always accounts for indexs for lists working from 0:number and for lengths to go from 1:number
        if month[m] == ('04' or '06' or '09' or '11'): #if months are april, june, september, or november
            if day[m] == '31': #if in that month the day is 31
                 #removes day, month, and year from list at same position as those four months cannot have 31 days
                day.remove(day[m])
                month.remove(month[m])
                year.remove(year[m])
        elif month[m] == '02': #if month is february, and days are greater than 28, remove incorrect date from list (only goes from 29-31 since 31 and greater has already been accounted for in the initial first test loop)
            if day[m] == ('29' or '30' or '31'):
                day.remove(day[m])
                month.remove(month[m])
                year.remove(year[m])
        else: #if none of the above conditions are met, date is valid and one is added to the counter m to iterate through next item of list
            m=m+1

    #Dealing with remaining valid dates

    #Each date has been tested at this point, if its valid it prints it

    for valid in range(len(year)): #print statement that iterates over the remaining valid dates and prints them
        print('Date Found: %s/%s/%s' % (str(day[valid]), str(month[valid]), str(year[valid])))

#Plug any string of text

test_dates = ('Anus farts on 31/05/2001 and gwen is born on 08/09/2003. The date 29/2/2004 does not exist! 04/05/3000 ')
isvalidDate(test_dates)
