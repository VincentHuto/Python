import random

print("Function to do insertion sort")


def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# Generate Random Array
def genRandomArray():
    genArray = []
    for i in range(100):
        genArray.append(random.randint(1, 999))
    return genArray


# Creating and Sorting Created Array
randArray = genRandomArray()
print("Random Array", randArray)
print("Sorted Array", insertionSort(randArray))
