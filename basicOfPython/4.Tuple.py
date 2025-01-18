# tuple and list are almost same, the only difference is tuple cannot be modified.
# data should always in between () and it can hold any (multiple)data type

values=(1,2,"Raj", 4,5)
print(values)    # [1, 2, 'Raj', 4, 5]

print(values[2]) # Raj

# it will print the last index data when used -1
# the formate is
# values : a, b, c, d
# index  : 0, 1 ,2, 3
# rev ind: 0,-3,-2,-1
print(values[-1]) # 5

# # Does not support for value insert in any index
# values.insert(3, "Karan")
# print(values)  # [1, 2, 'Raj', 'Karan', 4, 5]
#
# #  Does not support for update value at any index
# values[3] = "Chauhan"
# print(values) # [1, 2, 'Raj', 'Chauhan', 4, 5]
#
# # Does not support to append new values at the end
# values.append("End")
# print(values) # [1, 2, 'Raj', 'Chauhan', 4, 5, 'End']
#
# #  Does not supportto delete any values
# del values[6]
# print(values) # [1, 2, 'Raj', 'Chauhan', 4, 5]