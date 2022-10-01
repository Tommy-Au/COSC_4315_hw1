from functools import *
import sys
sys.setrecursionlimit(10000)

l_head = lambda l:l[0]
l_tail = lambda l:l[1:]

l_add = lambda x,y: x+y
l_sum = lambda l: reduce(l_add, l)

def readFile(filename):
    file1 = open(filename, "r").readlines()
    return file1

filename = 'input.txt'

l1 = readFile(filename)
print('Original input with newline')
print('l1 =', l1, '\n')

l2 = list(map(lambda l: l.split(), l1))
print('Array is created when newline')
print('l2 =', l2, '\n')

print('Combines seperated arrays into one')
l3 = l_sum(l2)
print('l3 =', l3, '\n')

l_split = lambda l: l.split(',')
print('Array is created when comma')
l4 = list(map(l_split, l3))
print('l4 =', l4, '\n')

l5 = l_sum(l4)
print('Combines seperated arrays into one')
print('l5 =', l5, '\n')

#original function working with other test cases
#is_period = lambda l: True if l[0] == '.' else (False if len(l) == 1 else is_period(l[1:]))
#period = list(filter(lambda l: is_period(l), l5))

#modified function to work with test case 2
is_period_s = lambda l: False if len(l) <= 1 else (True if l[0] == '.' else is_period_s(l[1:]))
period = list(filter(lambda l: is_period_s(l), l5))
print('Array of elements with period')
print('period =', period, '\n')

is_decimal = lambda l: True if l[0].isdigit() else (False if len(l) == 1 else is_decimal(l[1:]))
decimal = list(filter(lambda l: is_decimal(l), period))
print('Array of elements with decimal numbers')
print('decimal =', decimal, '\n')

print('Seperate array for integers')
integers = list(filter(lambda l: l.isdecimal(), l5))
print('integers =', integers, '\n')


#convert to int array and float array
int_arr = list(map(lambda l: int(l), integers))
real_arr = list(map(lambda l: float(l), decimal))
print('convert to int array and float array')
print(int_arr)
print(real_arr)
print('\n')

#searching
less_than = lambda a, b: a if a < b else b
get_min = lambda l: reduce(lambda l1, l2: less_than(l1, l2), l)
removed_min_arr = lambda l, minimum: list(filter(lambda p: p if p > minimum else False, l))
get_freq = lambda list1, list2: len(list1)-len(list2) if len(list1) >= len(list2) else len(list2)-len(list1)
freq = lambda l: get_freq(removed_min_arr(l, get_min(l)), l)
min_freq = lambda l: [get_min(l), freq(l)]

r1 = removed_min_arr(int_arr, get_min(int_arr))
r2 = removed_min_arr(r1, get_min(r1))
r3 = removed_min_arr(r2, get_min(r2))

print(min_freq(int_arr), int_arr)
print(min_freq(r1), r1)
print(min_freq(r2), r2)

freq_arr = lambda l: min_freq(l) if removed_min_arr(l, get_min(l)) == [] else min_freq(l) + freq_arr(removed_min_arr(l, get_min(l)))

f_int_arr = freq_arr(int_arr)
f_real_arr= freq_arr(real_arr)
print('frequency int array =', f_int_arr)
print('frequency real array =', f_real_arr)

f = (lambda l: [[l[0], l[1]]] if len(l) == 2 else [[l[0], l[1]]] + f(l[2:]))
print(f(f_int_arr))
print(f(f_real_arr))





















