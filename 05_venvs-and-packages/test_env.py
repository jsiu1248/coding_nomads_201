import cv
import pywhatkit
import numpy as np


#While a Python list can contain different data types within a single list, all of the elements in a NumPy array should be homogeneous. 
#NumPy arrays are faster and more compact than Python lists.
"""
array_example = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])"""

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
np.arange(2, 9, 2) # sort and specify the first and last number and step
# dtype when you want to specify the data type
# array_example.ndim shows the dimensions
# array_example.size - show total elements
#array_example.shape 