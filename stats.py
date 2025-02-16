from collections import Counter

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]
    return modes if len(modes) > 1 else modes[0]
