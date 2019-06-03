import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_br')
readFile = open('resposta3.txt','r')
writeFile = open('resposta5.txt','w')

for line in readFile:
    line = line.rstrip()
    div = line.split()

    rawDate = datetime.strptime(div[0], '%d/%m/%Y').date()

    formattedDate = rawDate.strftime('%Y/%m/%d')
    formattedInFullMonthDate = rawDate.strftime('%Y/%B/%d').upper()

    writeFile.write(formattedInFullMonthDate + ';' + formattedDate + '\n')

readFile.close()
writeFile.close()
