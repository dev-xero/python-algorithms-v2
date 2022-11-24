# Python Algorithms
👋🏼 Heya, I'm learning about data structures and algorithms using python.  
This is week 2 of my learning progress, I've created some basic algorithms and calculated their time complexities

## Algorithms
- [Simple Search](#simple-search)
- [Binary Search with sorting option (uses quicksort)](https://github.com/CodeNinja-tech/python-algorithms-v2#binary-search)
- [Quick Sort](https://github.com/CodeNinja-tech/python-algorithms-v2#quick-sort)

## Downloading the files
You could download the entire source code by clicking the green button, or alternatively in your terminal:
```bash
> git clone https://github.com/CodeNinja-tech/python-algorithms-v2.git
```
 This works **only if** you have git installed
 
<br>

## Simple Search
Simple search, from the name itself is actually a really simple algorithm.  
It works like this, suppose you have an array:
```python
a = [1, 2, 3, 4, 5]
```
Simple search goes through each of the items in the array until a match is found. Let's imagine the function looks something like this
```python
simple_search(arr=a, item=5)
```
As you can guess, simple search will have to go through the entire array before a match is found. 
That means that it goes through 1, compares 1 with the required item (in this case 5).  
Imagine what that would look like if we had an array of a biilion items, since it's time complexity is `O(n)`, in the worst case,  
it will run a **billion operations!** (and that is not very efficient) 

<br>

## Binary Search
Binary search is very fast, at least way faster than simple search as you will soon see. The way it works is by reducing the size of the array by 2 at each iteration.  
Again, let's use the same array as last time,
```python
a = [1, 2, 3, 4, 5]
```
Binary search differs from simple search in that at each iteration, our algorithm reduces the array like this:
```python
binary_search(arr=a, item=5)

returns: [4, 5]
returns: [5]
```
Wow, that's a lot faster because we only needed to check half the size of the array. Looking a bit deeper,  
Binary search looks for the mid point index, 2 in this case:
```python
a[2] = 3
```
It actually finds this by calculating the mid point at each iteration, kinda like this:
 ```python
 mid = (min + max) // 2
 # min is initally 0
 # max is the length of the array -1 i.e. len(arr) - 1
 ```
 
 It then compares the value of the mid point with the required item:
 ```python
 if arr[mid] == item:
    return mid  # the mid value is the required item
 elif arr[mid] < item:
    min = mid + 1  # the mid value is too low
 else:
    max = mid - 1  # the mid value is too high
 ```
So it does this until we reduce the arr to a single element or we find the value.  
Binary search is faster because it's time complexity is `O(log n)`, where `n` is the size of the array.  
So for an array of size 5, it takes log(5) to base 2 operations, which is approximately 2 operations at max just like we saw above.

The best part of binary search is that it scales really well, again, imagine we are searching an array with a billion items,  
log(10^9) base 2 is approximately 30 (which is miles faster than simple search!)  
so that means that in the worst case we'd only have to perform **30 operations!** (how awesome is that?)
 
<br>

## Quick Sort
Unlike the previous two, quick sort is a sorting algorithm and a powerful one at that (faster than selection sort). It uses Divide and Conquer to sort the array or input at the very basic level.  
Quick sort actually has a time complexity of `O(nlogn)` and `n` is still the size of the array.  
This algorithm is interesting because its time complexity can vary depending on where you choose to split the array from, that means at the:  
- **worst case it's O(n^2)** 
- **average case it's O(nlogn)**  
- **best case it's O(logn)**  

Quick sort tends to hit the average case more often than not so that's what we'll take the time complexity as.  
> NOTE: there is another fast algorithm that also uses divide and conquer, and that is merge sort but quick sort is usually faster than it in certain conditions

So let's use a new array this time that isn't sorted:

```python
u_list = [2, 3, 7, 8, 4, 9]
```

And let's also imagine our function is called like this:
```python
quick_sort(u_list)
```

Here's the output:
```python
returns: [2, 3, 4, 7, 8, 9]
```
Taking a closer peek at the function's body, the main meat of the algorithm is that it continuously splits the array in half, then creates two arrays, each  
of which values are either greater than the mid value or less than ( or equal to ) the mid value. It then sorts each sub array recursively by catenating the arrays:
```python
quick_sort(sm) + [arr[mid]] + quick_sort(lg)
# sm is a list of values less than or equal to the mid value
# lg is a list of values greater than the mid value
```

The body looks something like this
```python
mid = (len(arr) - 1) // 2  # mid index
new_arr = [:mid] + [mid+1:]  # build a new array but excluding the mid index value

sm = [i for i in new_arr if i <= arr[mid]]  # list comprehension to build an array of values less than or equal to the mid value
lg = [j for j in new_arr if j > arr[mid]]  # another list comprehension, but for values greater than the mid value

quick_sort(sm) + [arr[mid]] + quick_sort(lg)  # recursive call to sort again until the length of the array is less than 2

```
And the output? Of course! A sorted array because why not?
```python
returns: [2, 3, 4, 7, 8, 9]
```
> The concept of divide-and-conquer and also recursion can be a little difficult to grasp at first, check out the code for more clearity

<br>

## Thanks for reading, don't forget to ⭐ star the repo, it really helps a lot!

> Code provided in python
