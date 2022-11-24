# Time Complexity: O(n²)
def find_smallest(arr: list):
    i = 0
    for j in range(len(arr)):
        if arr[i] > arr[j]:
            i = j

    return i


def selection_sort(arr: list):
    new_arr = []
    for k in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


u_list = [2, 3, 7, 8, 4, 9]
print(selection_sort(u_list))
