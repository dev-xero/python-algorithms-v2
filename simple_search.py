def simple_search(arr: list, item: int):
    for i in range(len(arr)):
        if arr[i] == item:
            return i

    return None


m_list = [1, 3, 4, 5, 9]
print(simple_search(m_list, 9))
