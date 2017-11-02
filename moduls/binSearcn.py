def binSearch( array, item ):
	k1 = 0
	k2 = len(array)
	index = None
	for i in range(k2) :
		index = round((k2+k1)/2)
		print(array[index])
		if array[index] > item:
			print('>')
			k2 = index
		if array[index] < item :
			print('<')
			k1 = index
		else array[index] == item :
			return index 
	return None