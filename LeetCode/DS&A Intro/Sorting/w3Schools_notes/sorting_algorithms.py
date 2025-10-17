class Sorting_Algorithms():
    
    # =======================================================
    # BUBBLE SORT
    # =======================================================
    def bubble_sort(self, arr):
        
        # Grab the length of the arr
        n = len(arr)
        # go through each item, via the index (-1)
        for i in range(n-1):
            # everytime we go through each item, iterate through the entire list, 
            # but exclude the last position (because it's bubbled up in the prior step)
            for j in range(n-i-1):
                # For each iteration, compare two elements side by side and keep bringing up
                # the largets value you can
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def improved_bubble_sort(self, arr):

        n = len(arr)
        for i in range(n-1):
            # `swapped` is an flag of whether if a full pass goes 
            # without swapping values, then the list is already sorted
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    # =======================================================
    # SELECTION SORT
    # =======================================================
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            # Tabulate the minimum index we are on (right most position)
            min_index = i
            # Between the min-most to the end, go through each element
            for j in range(i+1, n):
                # If an element @ `j` is smaller than the value at the minimum `i`:
                if arr[j] < arr[min_index]:
                    # Grab that as the min-index value
                    min_index = j
            # Then pop the min-most value from the list
            min_value = arr.pop(min_index)
            # And insert it to the left-most position within the current frame
            arr.insert(i, min_value)
        return arr
    
    def improved_selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            # Improve time and space complexity by swapping immediately when a min value is found!
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
    def insertion_sort(self, arr):
        # Determine the length of arr
        arr_len = len(arr)
        # For each item in the range 1 -> length of arr
        for i in range(1, arr_len):
            # Determine that the insertion position is the current position you are iterating @
            insertion_pos = i
            # Then pop the item you are on 
            elem = arr_len.pop(i)
            # -- Handling the 'sorted array' to insert more values -- 
            # Within the range of the previous position, to -1 position, going backwards
            for j in range(i-1, -1, -1):
                # If an item within the 'sorted array' is larger than the current item
                if (arr[j] > elem):
                    # Set the insert index at the position found within 'sorted array'
                    insertion_pos = j
            # Then conduct the insertion
            arr.insert(insertion_pos, j)
        # return 
        return arr

    def improved_insertion_sort(self, arr):
        # Determine the length of arr
        arr_len = len(arr)
        # For each item in the range 1 -> length of arr
        for i in range(1, arr_len):
            # Determine that the insertion position is the current position you are iterating @
            insertion_pos = i
            # Then hold the item you are on (in a variable) 
            elem = arr_len[i]
            # -- Handling the 'sorted array' to insert more values -- 
            # Within the range of the previous position, to -1 position, going backwards
            for j in range(i-1, -1, -1):
                # If an item within the 'sorted array' is larger than the current item
                if (arr[j] > elem):
                # ------
                    # Move j over by one position 
                    arr[j+1] = arr[j]
                    # Set the insertion index to be @ `j`
                    insertion_pos = i
                # If not; then break the loop
                else: 
                    break
                # ------
            # Then set the held element to be at the insertion index (if not changed then the element stays in the same spot)
            arr.insert(insertion_pos, j)    
        # return     
        return arr 
    
    def quick_sort(self, arr):

        # Define a sub-function `partition()`, <- that will take in 
            #   <- arr
            #   <- low
            #   <- high
            #   -> index + 1
        

            # Initialize the pivot, which will be the value at the last position of the arr
            # Hold the position `i` of the -1 position of the sub-array
            # for elems between low and high range 
                # if the element is less than or equal to the pivot 
                # increment `i`
                # Then make a switch between elem and `i`
            # return `i`

        # Define `quicksort()`
        #   <- arr
        #   <- low; default to 0 
        #   <- high; default to None 
        #   -> None 

        # if high is None 
            # Then set high to be the length of the array (-1)
        # if low is less than high
            # hold the pivot index by calling `partition()`
            # recursively call quicksort(), but with pivot_index - 1 as the high
            # recursively call quicksort(), but with pivot_index + 1 as the low 

    def merge_sort(arr):

        # Define `mergeSort()` sub function 
        #   <- arr
        #   -> merge() call 

            # Grab the middle position of the arr
            # Grab the left-half of the arr (actual values)
            # Grab the right-half of the arr (actual values) (will contain the middle value too)

            # return by calling the merge() function on these two halves 

        # Define `merge()` sub function 
            # Initilize an empty `result` arr
            # set your counter variables `i` & `j` = 0 

            # While i is less than the length of the left sub-array and j is more than the length of the right array
                # If `i` in the left array is less than the `j` in the right array:
                    # Append item `i` in the left array into result arr
                    # increment `i`
                # If not: 
                    # append item `j` in the right array into result arr
                    # increment `j`
            
            # If the while condition is no longer possible; then place all items of left from `i` -> end 
            # Place all items of right from `j` -> onwards 

            # Return the result 

# TESTING 
algos = Sorting_Algorithms()
print(algos.bubble_sort([7,12,9,11,3]))

