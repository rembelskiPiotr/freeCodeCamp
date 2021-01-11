try:
    hours = float(input('Tell me hours: '))
except:
    print('Wrong input: not number')
    quit()
try:
    rate = float(input('Tell me rates: '))
except:
    print('Wrong input: not number')
    quit()
extraRate = rate * 1.5
overHours = hours - 40
if hours < 40:
    pay = hours * rate
else:
    pay = (40 * rate) + (overHours * extraRate)
print('Pay will be:', pay)
