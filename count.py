def count_frequency(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


arr = [10, 20, 10, 30, 20, 10]
print(count_frequency(arr))