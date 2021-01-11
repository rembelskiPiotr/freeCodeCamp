running_count = 0
running_total = 0.0
while True :
    user_input = input('Enter a number: ')
    if user_input == 'done' :
        break
    try:
        number = float(user_input)
    except:
        print('Invalid input')
        continue
    # print(number)
    running_count = running_count + 1
    running_total = running_total + number

# print('Job done!')
print(running_total,running_count,running_total/running_count)
