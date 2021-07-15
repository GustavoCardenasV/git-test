
number_list = input("Please enter the numbers, separated by ', ': ")
numbers = number_list.split(', ')
numbers.sort()

def sumLargestNumbers():
    sum_largest = int(numbers[-1]) + int(numbers[-2])
    return sum_largest

print (f"The largest numbers in the list are {n1} and {n2}, and the sum is {sumLargestNumbers()}")


