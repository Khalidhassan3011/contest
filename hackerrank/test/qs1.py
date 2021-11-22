import time


def mosharof_menu():
    print(".....MENU.....")
    print("1. Quick Sort")
    print("2. Binary Search")
    print("3. Exit")


def mosharof_partition(mosharof_arr, mosharof_low, mosharof_high):
    mosharof_i = (mosharof_low - 1)  # index of smaller element
    pivot = mosharof_arr[mosharof_high]  # pivot

    for j in range(mosharof_low, mosharof_high):

        # If current element is smaller than or
        # equal to pivot
        if mosharof_arr[j] <= pivot:
            # increment index of smaller element
            mosharof_i = mosharof_i + 1
            mosharof_arr[i], mosharof_arr[j] = mosharof_arr[j], mosharof_arr[i]

    mosharof_arr[mosharof_i + 1], mosharof_arr[mosharof_high] = mosharof_arr[mosharof_high], mosharof_arr[mosharof_i + 1]
    return mosharof_i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index


def mosharof_quick_sort(mosharof_arr, mosharof_low, mosharof_high):
    if len(mosharof_arr) == 1:
        return mosharof_arr
    if mosharof_low < mosharof_high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = mosharof_partition(mosharof_arr, mosharof_low, mosharof_high)

        # Separately sort elements before
        # partition and after partition
        mosharof_quick_sort(mosharof_arr, mosharof_low, pi - 1)
        mosharof_quick_sort(mosharof_arr, pi + 1, mosharof_high)


def mosharof_binary_search(mosharof_low, mosharof_high, mosharof_find_num):
    # Check base case
    if mosharof_high >= mosharof_low:

        mid = (mosharof_high + mosharof_low) // 2

        # If element is present at the middle itself
        if mosharof_numbers[mid] == mosharof_find_num:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif mosharof_numbers[mid] > mosharof_find_num:
            return mosharof_binary_search(mosharof_numbers, mosharof_low, mid - 1, mosharof_find_num)

        # Else the element can only be present in right subarray
        else:
            return mosharof_binary_search(mosharof_numbers, mid + 1, mosharof_high, mosharof_find_num)

    else:
        # Element is not present in the array
        return -1


mosharof_numbers = []
if __name__ == '__main__':
    while True:
        mosharof_menu()
        mosharof_input = input("Enter your choice ")

        if mosharof_input == "1":
            mosharof_total = int(input("Enter the number of elements "))
            print("Enter the elements of an array ")
            for i in range(0, mosharof_total):
                ele = int(input())
                mosharof_numbers.append(ele)
            mosharof_quick_sort(mosharof_numbers, 0, mosharof_total-1)
            mosharof_numbers.sort()
            print("Sorted Array is:")
            print(mosharof_numbers)

        elif mosharof_input == "2":
            mosharof_num = int(input("Enter the elements to be searched from the sorted array: "))
            mosharof_start_time = time.time()
            result = mosharof_binary_search(0, len(mosharof_numbers)-1, mosharof_num)
            mosharof_end_time = time.time()
            if result != -1:
                print(f"Element {mosharof_num} is found at position {result + 1}")
                print(f"Time taken is {mosharof_end_time - mosharof_start_time} CPU cycles")
            else:
                print("Element is not present in array")

        elif mosharof_input == "3":
            break;