nums = [2,3,4,1]


def even_sum(numbs):
    initial = 0
    for num in nums:
        if num % 2 == 0:
            initial += num
    return initial