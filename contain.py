def group_nums(list,n):
    for i in list:
        if n==i:
            return True
    return False
print(group_nums([2,5,8,9],5))
print(group_nums([2,8,9],5))   
