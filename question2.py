number1 = int(input('enter first integer: '))
number2 = int(input('enter second integer: '))
number3 = int(input('enter third integer: '))

if number1 > number2 and number2 > number3:
	maximum = number1 
	second_maximum = number2
	least_maximum = number3

elif number2 > number1 and number1 > number3:
	maximum = number2 
	second_maximum = number1
	least_maximum = number3

elif number3 > number1 and number1 > number2:
	maximum = number3
	second_maximum = number1
	least_maximum = number2


print('output:', least_maximum,end=',')
print(second_maximum,end=',')
print(maximum)




