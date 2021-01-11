def calculate_pay(hours,rate):
    extra_rate = rate * 1.5
    over_hours = hours - 40
    if hours < 40:
        pay = hours * rate
        return pay
    else:
        pay = (40 * rate) + (over_hours * extra_rate)
        return pay

hours = float(input('Tell me hours: '))
rate = float(input('Tell me rates: '))
print('Pay will be:', calculate_pay(hours,rate))
