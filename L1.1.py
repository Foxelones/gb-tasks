duration = int(input('Введи любое колличество цифр которое нужно будет переформатировать: >'))

days = duration // 3600 // 24
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60

text = "дни: {0}, часы: {1}, минуты: {2} секунды: {3} ".format(days, hours, minutes, seconds)

print(text)

