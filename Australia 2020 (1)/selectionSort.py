def findSmallest (arr):
	smallest = arr[0]   # for  keeping  the  most small element  
	smallest_index = 0  # for keeping the index of the most small meaning
	for i in range(1, len(arr)):  # we will go through whole array 
		if arr[i] < smallest:
			smallest = arr[i]  
			smallest_index = i
	return smallest_index   

def selectionSort(arr):
	new_arr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr
  		
a= selectionSort([5,2,3,4,24,56])
print (a)
			
