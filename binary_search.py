
# Implementation of binary search algorithm


# we will prove that binary search is faster than naive search


# Naive search : scans the entire list and ask if its equal to the target
# if yes return the Index
# if no then return -1
  
def naive_search(j, target):
      
    for i in range(len(j)):
        if l[i] == target:
            return i
    return -1

# Essence of binary search:
# If you have a sorted list and you want to search this array for something,
# You could go through each item in the list and ask, is this equal to what we're looking for?
# But we can make this *faster* by leveraging the fact that our array is sorted!
#  binary search is most about divide and conquer

def binary_search(j, target, high=None, low=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < j[midpoint]:
        return binary_search(j, target, low, midpoint -1)
    else:
        return binary_search(j, target, high, midpoint +1)

if __name__ == '__main__':
    
    l = [1,3,4,6,9]
    target = int(input("write"))
    print(naive_search(l, target))
    print(binary_search(l, target))
    
    # if binary_search(l, target):
    #     print()
    # else:
    #     print('Not found')

