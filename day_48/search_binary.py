def search_binary(arr:list, target: int) -> int:
    """ searches for a target number in a list and returns
        its index.
    """

    low, high = 0, len(arr) -1

    while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return f"the number {target} is at index {mid}"
            elif arr[mid] < target:
                low = mid + 1
            else:
                low = mid - 1
    return -1


list1 = [12, 34, 56, 78, 22, 45, 13]
print(search_binary(list1, 22))
