from functools import *
import sys
sys.setrecursionlimit(10000)

line = sys.argv[1]
k, input, output = line.split(';')

k = k[2:]
input = input[6:]
output = output[7:]


l_head = lambda l:l[0]
l_tail = lambda l:l[1:]

l_add = lambda x,y: x+y
l_sum = lambda l: reduce(l_add, l)

def readFile(filename):
    file1 = open(filename, "r").readlines()
    return file1

filename = 'input.txt'

#Original input with newline
l1 = readFile(filename)

#Array is created when newline
l2 = list(map(lambda l: l.split(), l1))

#Combines seperated arrays into one
l3 = l_sum(l2)

#Array is created when comma
l_split = lambda l: l.split(',')
l4 = list(map(l_split, l3))

#Combines seperated arrays into one
l5 = l_sum(l4)

#Array of elements with period
is_period_s = lambda l: False if len(l) <= 1 else (True if l[0] == '.' else is_period_s(l[1:]))
period = list(filter(lambda l: is_period_s(l), l5))

#Array of elements with decimal numbers
is_decimal = lambda l: True if l[0].isdigit() else (False if len(l) == 1 else is_decimal(l[1:]))
decimal = list(filter(lambda l: is_decimal(l), period))

#Seperate array for integers
integers = list(filter(lambda l: l.isdecimal(), l5))


#convert to int array and float array
int_arr = list(map(lambda l: int(l), integers))
real_arr = list(map(lambda l: float(l), decimal))

#searching for minimum, then creates new list without all occurences of that minimum, compare length of old list and new list to get freq of minimum
#do this until all frequency is obtained
less_than = lambda a, b: a if a < b else b
get_min = lambda l: reduce(lambda l1, l2: less_than(l1, l2), l)
removed_min_arr = lambda l, minimum: list(filter(lambda p: p if p > minimum else False, l))
get_freq = lambda list1, list2: len(list1)-len(list2) if len(list1) >= len(list2) else len(list2)-len(list1)
freq = lambda l: get_freq(removed_min_arr(l, get_min(l)), l)
min_freq = lambda l: [get_min(l), freq(l)]


freq_arr = lambda l: min_freq(l) if removed_min_arr(l, get_min(l)) == [] else min_freq(l) + freq_arr(removed_min_arr(l, get_min(l)))

f_int_arr = freq_arr(int_arr)
f_real_arr = freq_arr(real_arr)

#creates array with number paired with frequency
f = (lambda l: [[l[0], l[1]]] if len(l) == 2 else [[l[0], l[1]]] + f(l[2:]))
int_farr = f(f_int_arr)
real_farr = f(f_real_arr)


#selection sort
greater_than = lambda a, b: a if a[1] > b[1] else b
get_max = lambda l: reduce(lambda l1, l2: greater_than(l1, l2), l)
removed_max_arr = lambda l, max_arr: list(filter(lambda p: p if p[1] < max_arr[1] else False, l))
sorted_by_max = lambda l: get_max(l) if removed_max_arr(l, get_max(l)) == [] else get_max(l) + sorted_by_max(removed_max_arr(l, get_max(l)))

print('\n')
sorted_int = f(sorted_by_max(int_farr))
print(sorted_int)
sorted_real = f(sorted_by_max(real_farr))
print(sorted_real)

print('integers:')
l_list_asc = lambda n: [] if n == 0 else l_list_asc(n-1) + [n]
k = 3
k_list = l_list_asc(k)
l_print = lambda l, k_list: list(map(lambda k: print(l[k-1]), k_list))
l_print(sorted_int, k_list)

print('real:')
l_print(sorted_real, k_list)




















