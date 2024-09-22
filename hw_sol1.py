######################## input 10 numbers in range
counter: int = 0
positive: int = 0
negative: int = 0
zeros: int = 0
div_7: int = 0
last_positive: int = None
last_negative: int = None
SENTINEL: int = -999
NUMBERS_MAX: int = 5
for _ in range(10):
    number: int = int(input('enter a number: '))
    if number == SENTINEL:
        break
    # if number < -1000 or number > 1000
    if not -1000 <= number <= 1000:
        print('number not in range, skipping ...')
        continue
    counter += 1
    if number % 7 == 0:
        div_7 += 1
    if number > 0:
        positive += 1
        last_positive = number
    elif number < 0:
        negative += 1
        last_negative = number
    else:
        zeros += 1
else:
    # not break
    print(f"positive count: {positive}")
    print(f"negative count: {negative}")
    print(f"last positive count: {last_positive}")
    print(f"last negative count: {last_negative}")
    print(f"divided by 7: {div_7}")
    print(f"zeros: {zeros}")


######################## input 10 numbers in range
counter: int = 0
positive: int = 0
negative: int = 0
zeros: int = 0
div_7: int = 0
last_positive: int = None
last_negative: int = None
SENTINEL: int = -999
NUMBERS_MAX: int = 10
while counter < NUMBERS_MAX:
    number: int = int(input('enter a number: '))
    if number == SENTINEL:
        break
    # if number < -1000 or number > 1000
    if not -1000 <= number <= 1000:
        print('number not in range, skipping ...')
        continue
    counter += 1
    if number % 7 == 0:
        div_7 += 1
    if number > 0:
        positive += 1
        last_positive = number
    elif number < 0:
        negative += 1
        last_negative = number
    else:
        zeros += 1
else:
    # not break
    print(f"positive count: {positive}")
    print(f"negative count: {negative}")
    print(f"last positive count: {last_positive}")
    print(f"last negative count: {last_negative}")
    print(f"divided by 7: {div_7}")
    print(f"zeros: {zeros}")
