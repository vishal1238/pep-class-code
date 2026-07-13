def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# binary_search
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid=(low+high)//2
        if target == data(mid):
            return True
        elif target < data(mid):
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, (mid+1),high)


# binary_search_interative
def binary_search_interative(data, target):
    low = 0
    high = len(data-1)
    while low <= high:
        mid = (low + high)//2
        if target == data(mid):
            return True
        elif target < data(mid):
            high = mid - 1
        else:
            low = mid + 1
    return False



# insertion_sort
def insertion_sort(a):
    for i in range(1,len(a)):
        cur = a(i)
        j=i
        while j>0 and  a(j-1)>cur:
            a(j) = a(j-1)
            j -= 1
            a(j)=cur
