def sort(arr: list):
    if len(arr) < 2:
        return arr

    mid = (len(arr) - 1) // 2

    pivot = arr[mid]
    x_list = arr[:mid] + arr[mid+1:]  # The list without the middle item

    sm = [i for i in x_list[0:] if i <= pivot]
    lg = [j for j in x_list[0:] if j > pivot]

    return sort(sm) + [pivot] + sort(lg)


def binary_search(arr: list, item: int, _sorted=False):
    # Binary Search works best with sorted arrays

    # Quick Sort the array
    _list = sort(arr) if _sorted else arr

    _min = 0
    _max = len(_list) - 1

    while _min <= _max:
        mid = (_min + _max) // 2

        print(_list[_min:_max+1])

        if _list[mid] == item:
            return mid
        elif _list[mid] > item:  # Too high, reduce the max
            _max = mid - 1
        else:  # Too low, increase min
            _min = mid + 1

    return None


m_list = [3, 2, 9, 10, 11, 10]
print(binary_search(m_list, 10, _sorted=False))
