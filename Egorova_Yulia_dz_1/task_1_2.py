numbers = []

for number in range(1, 1000, 2):
    number = number ** 3
    numbers.append(number)
print(numbers)

sum_range = 0
sum_range_17 = 0
for number in numbers:
    sum = 0
    num = number
    while num != 0:
        sum = (sum + (num % 10))
        num = num // 10
    if sum % 7 == 0:
        sum_range = sum_range + number
print(sum_range, 'сумма чисел, сумма цифр, которых делится на 7')
for number in numbers:
    sum = 0
    number += 17
    num = number
    while num != 0:
        sum = (sum + (num % 10))
        num = num // 10
    if sum % 7 == 0:
        sum_range_17 += number
print(sum_range_17, 'сумма чисел после прибавления 17')
