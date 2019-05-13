def binary_search(list, item):
    high = len(list) - 1
    low = 0
    while low <= high:
        mid = (high - low) // 2 + low
        guess = list[mid]
        if guess == item :
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
    return None

my_list = [2, 4, 7, 9, 11]
binary_search(my_list, 11)