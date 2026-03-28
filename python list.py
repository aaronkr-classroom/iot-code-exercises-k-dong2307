my_list = [10, 20, 30, 40]

print(my_list[0])
print(my_list[2])

my_list.append(50)
print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list.remove(30)
print(my_list)

del my_list[2]
print(my_list)

print(len(my_list))

for item in my_list:
    print(item)
    
sub_list = my_list[1:3]
print(sub_list)