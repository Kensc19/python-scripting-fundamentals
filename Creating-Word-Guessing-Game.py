#!/usr/bin/env python3

def consent():
    answer = input('Would you like to know how old you will be in a particular year? (y/n)')

    while not (answer == 'y' or answer == 'n'):
        print("I'm sorry, I didn't understand. Please try again.")
        answer = input('Would you like to know how old you will be in a particular year? (y/n)')

    if answer == 'n':
        print("I'm sorry you're not interested. Goodbye!")
        valid = False
    else:
            valid = True
    return valid

def obtainDate(prompt):
    dateValid = False
    while dateValid is False:
        print("Valid formats for dates: '1/1/2000' or 'jan 1, 2000'")
        if prompt == 'dob':
            string = 'What is your birthday?'
        if prompt == 'future':
            string = 'What date did you want to know about?'
        date = input(string)
        dateValid = validateDate(date)
        if bool(dateValid) is False:
            print("I'm sorry that is not a valid date.")
            print("")

    return date

def parseDate(date):
     if date[0].isdigit() is True:
            tempDate = date.split('/')
            month = tempDate[0]
            year = tempDate[2]
            day = tempDate[1]
     else:
            tempDate = date.split()
            month = tempDate[0]
            year = tempDate[2]
            day = ''
            for i in tempDate[1]:
                if i != ',':
                    day = day + i
            month = convertMonth(month)
            
     return month, day, year

def convertMonth(month):
    months = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
   
    if month[0:3].lower() in months:
        month = months.index(month[0:3].lower())
    else:
        month = 'notValid'
        return month

    return month

def validateDate(date):
    dateValid = False
    dayValid = False
    monthValid = False
    yearValid = False
    longMonths = [1, 3, 5, 7, 8, 10, 12]
    shortMonths = [4, 6, 9, 11]

    if date[0].isdigit() is True:
        tempDate = date.split('/')
    else:
        tempDate = date.split()
    if len(tempDate) < 3:
        return dateValid
    
    month, day, year = parseDate(date)

    if month == 'notValid':
        return dateValid

    month = int(month)
    day = int(day)
    year = int(year)

    if month > 0 and month <= 12:
        monthValid = True
    if month in longMonths:
        if day <= 31 and day != 0:
            dayValid = True
    elif month in shortMonths:
        if day <= 30 and day != 0:
            dayValid = True
    elif month == 2:
        if day <= 29 and day != 0:
            dayValid = True
    if year > 1900:
        yearValid = True
    
    if monthValid is True and dayValid is True and yearValid is True:
        dateValid = True

    return dateValid

print('Welcome to the age calculator.')
valid = consent()


if valid is True:
    dates = []

    dob = obtainDate('dob')
    dates.append(dob)
  
    future = obtainDate('future')
    dates.append(future)

    month = ['', '']
    day = ['', '']
    year = ['', '']
    
    month[0], day[0], year[0] = parseDate(dates[0])
    month[1], day[1], year[1] = parseDate(dates[1])
            
    month[0] = int(month[0])
    month[1] = int(month[1])
    
    age = int(year[1]) - int(year[0])
    day[0] = int(day[0])
    day[1] = int(day[1])
    if month[1] <= month[0]:
        age = age - 1
        if month[1] == month[0]:
            if day[1] >= day[0]:
                age = age + 1

    results = 'On {} you will be {} years old.'

    print(results.format(dates[1], age))
    print('Goodbye!') 