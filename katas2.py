
numbers_list = input("Please enter your numbers, separated by a coma (', '): ")
condition = input("PLease state the condition you want ('even' or 'odd'): ")

def conditionalSum(numbers_list, condition):
    list_even = []
    list_odd = []
    number = numbers_list.split(', ')
    for n in number:
        if int(n) % 2 == 0:
            list_even.append(int(n))
        else:
            list_odd.append(int(n))
    if condition == 'even':
        even_sum = sum(list_even)
        return print(even_sum)
    elif condition == 'odd':
        odd_sum = sum(list_odd)
        return print(odd_sum)
    else:
        return print('0')

conditionalSum(numbers_list, condition)