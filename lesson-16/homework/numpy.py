import numpy as np
# 1
my_list = [12.23, 13.32, 100, 36.32]
my_array = np.array(my_list)
type(my_array)
# 2
my_array = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
my_array
# 3
zero_vector = np.array([0]*10)
zero_vector[5] = 11
zero_vector
# 4
# Creates a numpy array with numbers ranging from 12 to 38 amd assings to a variable 'arr'
arr = np.arange(12, 38)
arr
# 5
arr1 = np.array([1, 2, 3, 4])
floating_array = np.astype(arr1, 'float')
floating_array
# 6


def fah_to_cel(lst):
    if type(lst) != 'numpy.ndarray':
        arr = np.array(lst)
    else:
        arr = lst
    c = (arr - 32) * (5/9)
    for i, n in enumerate(c):
        c[i] = round(n, 2)
    return c


def cel_to_fah(lst):
    if type(lst) != 'numpy.ndarray':
        arr = np.array(lst)
    else:
        arr = lst
    f = (arr * (9/5)) + 32
    for i, n in enumerate(f):
        f[i] = round(n, 2)
    return f


# 7
# A test array to aapned vlues to
my_array = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9), dtype='int8')
# makes a copy of the initial array and appneds the given values to the end of the array, such that original array stays unmodified
new_array = np.append(my_array, (10, 11, 12, 13, 14, 15))
# 8
arr = np.random.randint(0, 50, size=(1, 10))
print(arr)
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
print(f'Mean: {mean}')
print(f'Median: {median}')
print(f'Standard deviation: {round(std, 2)}')
# 9
# Creates an array of 10x10 size with random numbers form 0 to 50
my_array = np.random.randint(0, 50, size=(10, 10))
print(my_array)
# NumPy function that finds the max value from an array
maximum = np.max(my_array)
# NumPy function that finds the min value from an array
minimum = np.min(my_array)
print(maximum)
print(minimum)
# 10
# Creates a 3x3x3 array with tandom values from 0 to 10
arr3d = np.random.randint(0, 10, size=(3, 3, 3))
