# A1

# age = int(input())
# print('In 5 years you will be', str(age + 5), 'years old')

# A2
# 원인 : num1 이 변수로 정의되지 않았기에 출력이 불가능하다.

# def average(num1, num2, num3):
#     return (num1 + num2 + num3) / 3

# num1, num2, num3 = 7, 5, 9
# print(average(num1, num2, num3))
# num1, num2, num3 = 6, 6, 7
# print(average(num1, num2, num3))
# print(num1)

# A3

def IceCreamPrice(scoops):
    return scoops * 1.15 + 2.25

print('Ice cream cone pricce calculator:')
scoops = int(input('How many scoops would you like? '))
print('A %d-scoop cone will cost $%.2f'%(scoops, IceCreamPrice(scoops)))
