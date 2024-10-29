# Sorting Algorithms

# Bubble Sort


'''1. Define the function bubble_sort(array):
    2. Set n to the length of the array.
    3. For i from 0 to n - 1, do the following:
       a. For j from 0 to n - i - 1, do the following:
            i. If array[j] > array[j + 1], then:
                A. Swap array[j] and array[j + 1].
                 # Swap elements if they are in the wrong order
                  
                arr[j] and arr[j+1] represent the current element (arr[j]) and the next element (arr[j+1])
                 in the array, respectively. The right side of the assignment (arr[j+1], arr[j]) creates a tuple 
                 containing the next element (arr[j+1]) and the current element (arr[j]) in that order. On the 
                 left side of the assignment, arr[j] and arr[j+1] are being assigned the values of 
                 arr[j+1] and arr[j], respectively, effectively swapping their positions in the array.
                So, in simpler terms, this line swaps the positions of arr[j] and arr[j+1] if they are 
                in the wrong order, ensuring that the smaller element moves towards the beginning of 
                the array while the larger element moves towards the end, thereby gradually "bubbling" 
                the largest elements to the end of the array. 
    4. Return the sorted array. '''


#pros: simple and intuituve, stable, low memeory usage
#cons: bad for large datasets, slow, not often used in real world applications

def bubble_sort(array): #defining the function
    n = len(array)  #setting the length of the array to the variable n 
    for i in range(n):  # looping through the array for how much is within it 
        for j in range(n - i - 1):  # moves through the array 
            if array[j] > array[j + 1]: #checks if the new number it is checking is bigger or smaller then the already sorted numbers
                array[j], array[j + 1] = array[j + 1], array[j] #changes the position if the new number is bigger putting it near the end of the array
    return array

arr1 = [64, 34, 25, 12, 22, 11, 90, 98, 56, 108, 203, 2, 0]
bubble_sort(arr1)
print("Bubble Sort:", arr1)











                
# Selection Sort n should be the lenght of the array
'''1. Define the function selection_sort(array):
    2. Set n to the length of the array.
    3. For i from 0 to n - 1, do the following:
        a. Set min_index to i.
        b. For j from i + 1 to n - 1, do the following:
            i. If array[j] < array[min_index], then:
                A. Set min_index to j.
        c. If min_index is not equal to i, then:
            i. Swap array[i] and array[min_index].
    4. Return the sorted array.
'''
# https://www.geeksforgeeks.org/selection-sort-algorithm-2/
#pros: simple, less swapping of numbers/slots of the array
#cons: slow, does not maintain the relative order of equal elements


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i #sets the position that will be looked at in the array

        # this loop goes through the whole array and finds the smallest number out of the remaining ones in the array
        # and sends the smallest one to the front if it is smaller then the already found smallest if not it will be in the next position behind the smallest in the array
        for j in range(i + 1, n):   
            if array[j] < array[min_index]:
                min_index = j
            if min_index != i: 
                array[i], array[min_index] = array[min_index], array[i]
    return array
arr2 = [64, 34, 25, 12, 22, 11, 90, 98, 56, 108, 203, 2, 0]
selection_sort(arr2)
print ("Selection Sort:", arr2)
        


    

'''
# Insertion Sort

1. Define the function insertion_sort(array):
    2. For index from 1 to length(array) - 1, do the following:
        a. Set current_value to array[index].
        b. Set position to index.
        c. While position > 0 and array[position - 1] > current_value:
            i. Set array[position] to array[position - 1].
            ii. Decrement position by 1.
        d. Set array[position] to current_value.
    3. Return the sorted array.
'''
#https://www.simplilearn.com/tutorials/data-structure-tutorial/insertion-sort-algorithm#what_are_the_advantages_of_the_insertion_sort
#https://dbmspoly.blogspot.com/p/advantage-disadvantages-of-sort.html
#pros: effective on small data sets, simple, takes up minmal space
#cons: inefective with hugh data sets, slow as it has to go from the start to the end of the array and even more times if say the alst number in the array was the smallest and had to move all the way to the front
#in a hugh array

#moves the current number in the arary to the front and then goes to the next bringing it forward till it hits a number smaller then it and repeats thatt process until sorted
def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index] 
        position = index  
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]  
            position -= 1  
        array[position] = current_value
    return array
arr3 = [64, 34, 25, 12, 22, 11, 90, 98, 56, 108, 203, 2, 0]
insertion_sort(arr3)
print("Insertion Sort: ", arr3)


'''
# Searching Algorithms

# Sequential Search
# https://www.youtube.com/watch?v=19hcyQN8J7o

1. Define the function sequential_search(array, target):
    2. For each element in the array, do the following:
        a. Compare the current element with the target.
        b. If the current element is equal to the target:
            i. Return the index of the current element.
    3. If the loop completes and the target is not found:
        a. Return -1 to indicate the target is not in the array.
'''

#https://mrdorancomputing.com/algorithms/searching-algorithms/
#pros: Does not require the data to be sorted, Could be fast if the search item is towards the beginning of the list.
#cons: slow - each item may need to be checked

# with linear search it goes through the whole array checking each number/slot to find a matching "target"
# if it is found it will return true if the target is not found it will return false

def sequentialSearch(l, target):
    n = len(l)
    for i in range(0, n):
        if l[i] == target:
            return True
    return False

arr4 = [2,4,3,40,10]
targetNum1 = sequentialSearch(arr4, 10)
print("SequentialSearch 1: ", targetNum1)

arr5 = [2, 4, 3, 40, 10, 49, 57, 103, 205]
targetNum2 = sequentialSearch(arr5, 69)
print("SequentialSearch 2: ", targetNum2)






'''
# Binary Search (iterative)
# https://www.youtube.com/watch?v=DnvWAd-RGhk&t=199s
1. Define the function binary_search(array, target):
    2. Set low to 0.
    3. Set high to length(array) - 1.
    4. While low <= high, do the following:
        a. Set mid to the integer division of (low + high) by 2.
        b. If array[mid] is equal to target:
            i. Return mid.
        c. Else if array[mid] is less than target:
            i. Set low to mid + 1.
        d. Else:
            i. Set high to mid - 1.
    5. If the target is not found, return -1.
'''

#pros: fatser then sequntial/linear search on large datasets
#cons: dataset must be sorted before starting


# binary search goes to the middle of the array to find the taret number, if it isnt there it ignores the other half of the string
# (eg 1,4,5,8,10 if you were looking for 4 it starts at 5 then ignores 8,10 then if you were looking for 10 it would start at 5 and then ignore 1,4)
# from there it goes to the middle of the part of the array that wasnt ingored and continues like that untill it finds the target

def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "NONE"

arr6 = [1,2,4,6,7,9]
targetNum3 = 4
result = (binarySearch(arr6, targetNum3))
print("BinarySearch: Possition in array =", result)

'''Task: 
Part 1 Research the purpose and function of each of the supplied algorithms.

Once you comprehend these rewrite the supplied algorithms in Python and create a main program that executes each of them to demonstrate their function.

2. Add additional comments to make it clear exactly what is happening, for example the comment in the bubble sort.

3. Explain any limitations of the Sort and Search algorithms in the header comments that explain the function. 

4. For the following two snippets re-write them without using any inbuilt helper functions e.g. the 
Python provided insert and del (delete) functions, to acheive the same result. Comment clearly their operation.

NOTE you will be required to explain their operation to the lecturer so DON'T use Chat GPT, you need to learn this stuff!!
'''
'''

arr = [1, 2, 3, 4, 5]
arr.insert(2, 10)  # Insert 10 at index 2
print("After insertion:", arr)
'''

def insertAtIndex(arr, index, element):
    #add an extra slot to the end of the array
    arr += [0]
    
    #move the existing elements to the right to make space for the new item
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    
    #insert the new item 
    arr[index] = element
    
    return arr

arr7 = [1, 2, 3, 4, 5]
arr7 = insertAtIndex(arr7, 2, 10)
print("arr7 After insertion:", arr7)


'''
arr = [1, 2, 3, 4, 5]
del arr[2]  # Delete element at index 2
print("After deletion:", arr)
'''

#learnt about arr[:-1] from here https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
def removeAtIndex(arr, index):
    #shifts elements to the left to overwrite the element at 'index'
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    
    #looks at the array from the perspective of 1,2,3 and removes the last item
    return arr[:-1]

arr8 = [1, 2, 3, 4, 5]
arr8 = removeAtIndex(arr8, 2)
print("arr8 After removal:", arr8)


#old ones 

#list1 = []
#list1 = list1 + [1] #add 1 to the list
#list1 += [3] #add 3 to the list
#print("List1: ", list1) #write out the list after having values added to it 

#list2 = [1, 2, 3, 4, 2]
# goes through the array and checks to see what numbers do not match the given number
# and keeps the ones that do not match while removing the one/s that do match 
#list2 = [x for x in list2 if x != 2]  
#print("List2: ", list2)