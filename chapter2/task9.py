four = 4
eight = 8
multiplesfour = 1
multipleseight = 1
summultiplesfour = 0
summultipleseight = 0
newsum = 0
square = 1


for i in range (5):
	multiplesfour = multiplesfour * four
	summultiplesfour += multiplesfour
	multipleseight = multipleseight * eight
	summultipleseight += multipleseight
newsum = summultiplesfour + summultipleseight
square = newsum * newsum
print(square)
	
	
