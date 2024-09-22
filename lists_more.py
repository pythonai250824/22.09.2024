import random
import statistics

# index:               0  1   2  3   4   len == 4
numbers: list[int] = [10, 2, -1, 12] #Error
print(numbers)
print('numbers[0]:', numbers[0])  # 10
print('numbers[1]:', numbers[1])  # 2
print('numbers[2]:', numbers[2])  # -1
print('numbers[3]:', numbers[3])  # 12
#print(numbers[4])  # IndexError: list index out of range

print('numbers[ len(numbers) - 1 ]:', numbers[ len(numbers) - 1])  # last item

# create a list of random numbers
#import random
#random.choices(range(1, 10), k=10)

# create a list of 10 numbers from 1-10 with square 1*1, 2*2, 3*3, 4*4 ... 10*10
numbers_1_10: list[int] = []
for i in range(1, 10 + 1):
    numbers_1_10.append(i ** 2)
print('numbers_1_10:', numbers_1_10)

# create a list of 10 random numbers , each number between 1-100
numbers_random: list[int] = []
for _ in range(10):
    #                    2          1
    # numbers_random.append(random.randint(1, 100))
    rand_number = random.randint(1, 100)
    numbers_random.append(rand_number)

print('numbers_1_10:', numbers_1_10)

# 1. create an empty list. input 10 numbers from the user and append them into the list
#    print len, max, min, statistics.mean
list_user: list[int] = []
for _ in range(15):
    num: int = int(input('enter number: '))
    list_user.append(num)

print('len', len(list_user))
print('max', max(list_user))
print('min', min(list_user))
print('mean', statistics.mean(list_user))

# 1.5.a find the max numbers without max function
max_number: int = list_user[0]  # the max number is the first element
for i in range(1, len(list_user)):  # 1-9
    if list_user[i] > max_number:
        max_number = list_user[i]
print('maximum is', max_number)

# 1.5.b. go over the list and print all numbers % 2 == 0
for i in range(len(list_user)):  # 1-9
    if list_user[i] % 2 == 0:
        print(list_user[i])

# 2. create an empty list. run from 1 to 10 , append random.choice([1, 4, 9, -2])
#    print statistics.mean
