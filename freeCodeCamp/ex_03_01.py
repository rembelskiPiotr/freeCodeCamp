hours = float(input('Tell me hours: '))
rate = float(input('Tell me rates: '))
extraRate = rate * 1.5
overHours = hours - 40
if hours < 40:
    pay = hours * rate
else:
    pay = (40 * rate) + (overHours * extraRate)
print('Pay will be:', pay)
