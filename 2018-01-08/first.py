print('hello world')

def add(num1, num2):
    return num1 + num2

print(add(2,3))


def rec_vol(length, width, height):
    return(length * width * height)

def mean(numbers):
    return(sum(numbers)/len(numbers))

'''
def median(numbers):
    import math
    slist = sorted(numbers)
    if len(slist) % 2 == 1:
        return(slist[(math.ceil(len(slist)/2)) -1])
    if len(slist) % 2 == 0:
        empty_list = []
        empty_list.append(slist[int(len(slist)/2)])
        empty_list.append(slist[int(len(slist)/2) - 1])
        return(mean(empty_list))
'''

def median(numbers):
    """Computes the median of a list of numbers.

    argument: list of numbers
    return: the median

    >>> median([2,1,6])
    2
    >>> median([3,5,4,9])
    4.5
    """
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        # even list
        return sum(numbers[middle - 1:middle + 1]) / 2
    else:
        # odd list
        return numbers[middle]


def mode(numbers):
    """ Find the most common value in the list

    argument: list of numbers
    return: the mode

    >>> mode([1,2,2,2,33,4])
    2
    """
    from collections import defaultdict
    d = defaultdict(int)
    for el in numbers:
        d[el] += 1
    return(sorted(d, key=lambda key: d[key], reverse=True)[0])
    
