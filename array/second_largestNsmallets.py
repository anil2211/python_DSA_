def max_min(list): 
	largest = list[0] 
	lowest = list[0] 
	largest2 = None
	lowest2 = None
	for i in list[1:]:
		if i > largest: 
			largest2 = largest
			largest = i 
		elif largest2 is None or largest2 < i: 
			largest2 = i
		if i < lowest: 
			lowest2 = lowest
			lowest = i 
		elif lowest2 is None or lowest2 > i: 
			lowest2 = i 
			
	print("Largest element is:", largest) 
	print("Smallest element is:", lowest) 
	print("Second Largest element is:", largest2) 
	print("Second Smallest element is:", lowest2) 


# Driver Code
list = [12, 45, 2, 41, 31, 10, 8, 6, 4]
max_min(list)
