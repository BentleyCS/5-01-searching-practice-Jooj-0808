import random

def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    if not items:
        return -1  # Handle empty list case

    tries = 0

    while True:
        tries += 1
        random_index = random.randint(0, len(items) - 1)
        selected_item = items[random_index]

        if selected_item == target:
            print(tries)
            return random_index
        else:
            print(tries)

def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    checks_count = 0
    for index, value in enumerate(items):
        checks_count += 1
        if value == target:
            return index, checks_count

    return -1, checks_count


def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements binary search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    first = 0
    last = len(items) - 1
    checks = 0

    while first <= last:
        mid = (first + last) // 2
        checks += 1

        if items[mid] == target:
            return mid, checks
        elif target < items[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return -1, checks
