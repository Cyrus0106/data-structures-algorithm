import array

my_array = array.array('i')
print(my_array)
my_array1 = array.array('i', [1, 2, 3, 4, 5])
print(my_array1)

import numpy as np

np_array = np.array([], dtype=int)
print(np_array)

np_array1 = np.array([1, 2, 3, 4, 5])
print(np_array1)

# time complexity of creating an array is O(1) because it is contastant
# space complexity of creating an array is O(1) because it is contastant
# time complexity of creating an array with elements is O(n) because it is linear