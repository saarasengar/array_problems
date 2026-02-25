def secondlargest(arr):

    if len(arr) < 2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second


arr = [10, 5, 20, 8, 20]
print(secondlargest(arr))




