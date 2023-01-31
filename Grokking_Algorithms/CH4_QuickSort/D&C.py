# Given an array, give the total

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


# =============================================================
# =========== E X E R C I S E S ===============================
# =============================================================

# 4.1:
# Sum elements in a list
def recursive_sum(arr):
    index = len(arr) - 1
    if arr == []:  # base case
        return 0
    else:
        return  arr[0] + recursive_sum(arr[1:])  # recursive case 

print(recursive_sum([4,7,3,6])) 
# R E F E R E N C E:
# https://stackoverflow.com/questions/27652686/python-what-does-for-x-in-a1-mean


# 4.2
# Count elements in a list
def count_elements(list):
    if list == []:
        return 0
    else:
        return 1 + count_elements(list[1:])


print(count_elements([4,7,3,6])) 


# 4.3
# Find the maximun number in a list
def max_value(list): 
    if list == []:
        return None
    if len(list) == 1:
        return list[0]
    else:
        sub_max = max_value(list[1:])
        return list[0] if list[0] > sub_max else sub_max

print(max_value([4,7,3,6,40])) 