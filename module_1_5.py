immutable_var = tuple([1, 'eeee', True])
print(immutable_var)

# Изменение элементов кортежа невозможно, так как кортеж относится к неизменяемым типам,
# но он может содержать в себе изменяемые типы
mutable_list = [1, 3, True]
print(mutable_list)

mutable_list[0] = 'ddd'
mutable_list[1] = False
mutable_list[2] = 99
print(mutable_list)