#sorting is a way to arrange data in a specific order. It can be done in ascending or descending order.
#Python provides built-in functions to sort data, such as sorted() and list.sort().
#sorted() returns a new sorted list from the items in an iterable.
#list.sort() sorts the list in place and returns None.
#Example of sorted() function

import numpy as np


numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)



#Example of list.sort() method
numbers = [5, 2, 9, 1, 5, 6]
print("Sorted numbers:", np.sort(numbers))

#Sorting a 2D array
arr = np.array([[3, 2], [1, 4]])
print("sorting 2 D array:", np.sort(arr)) #sort by column