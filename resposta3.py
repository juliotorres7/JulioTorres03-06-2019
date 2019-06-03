import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_br')
readFile = open('resposta2.txt','r')
writeFile = open('resposta3.txt','w')

for line in readFile:
    line = line.rstrip()
    rawDate = datetime.strptime(line, '%d/%m/%Y').date()
    formattedDate = rawDate.strftime('%d/%B/%Y').upper()

    writeFile.write(line + ' - ' + formattedDate + '\n')

readFile.close()
writeFile.close()
