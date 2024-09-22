
#              index  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
#              index   0   1   2   3   4   5   6   7   8   9    10
my_list: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('[ my_list[0], my_list[1], my_list[2] ]-->', [ my_list[0], my_list[1], my_list[2] ])
print('my_list[0: 3]-->', my_list[0: 3])
print('my_list[:3]-->', my_list[:3])  # range(0, 10) range(10)
print('my_list[:10]-->', my_list[:10])
print('my_list[:len(my_list)]-->', my_list[:len(my_list)])
print('my_list[:9]-->', my_list[:9])  # -1 ==> index 9
print('my_list[:-1]-->', my_list[:-1], 'like index 9')  # -1 ==> index 9
print('my_list[:]-->', my_list[:], 'like my_list[0:10] len == 10')
print('my_list[3:]-->', my_list[3:], 'like my_list[3:10] len == 10')
print('my_list[3::2]-->', my_list[3::2], 'like my_list[3:10] len == 10') # range(1, 10, 2)
print('my_list[3::-1]-->', my_list[-1::-1], 'like my_list[-1::-1]') # range(1, 10, 2)
print('my_list[-2]-->', my_list[-2])

my_list.insert(5, 555)
#              index     0   1   2   3   4   5   6   7   8   9    10
# my_list: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#                        0   1   2   3   4   5  ->  6   7   8   9   10
# my_list: list[int] = [10, 20, 30, 40, 50, 555,-> 60, 70, 80, 90, 100]
print(my_list)
