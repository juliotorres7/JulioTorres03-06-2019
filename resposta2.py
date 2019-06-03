import datetime
import calendar

counter = 0
firstDate = datetime.date(datetime.datetime.now().year, 1, 1)
file = open('resposta2.txt','w')

if calendar.isleap(firstDate.year):
    numberOfDaysInYear = 366
else:
    numberOfDaysInYear = 365

while counter < numberOfDaysInYear:
    day = firstDate.strftime('%d')
    month = firstDate.strftime('%m')
    year = firstDate.strftime('%Y')

    file.write(day + '/' + month + '/' + year + '\n')

    firstDate += datetime.timedelta(days=+1)
    counter += 1

file.close()
