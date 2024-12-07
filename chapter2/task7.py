four = 4
eight = 8
multiplesfour = 1
multipleseight = 1
summultiplesfour = 0
summultipleseight = 0


for i in range (5):
	multiplesfour = multiplesfour * four
	summultiplesfour += multiplesfour
	multipleseight = multipleseight * eight
	summultipleseight += multipleseight
print(summultiplesfour, end=" ")
print(summultipleseight)
	
	
