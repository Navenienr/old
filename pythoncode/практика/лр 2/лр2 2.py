number_1 = int(input("ввведите первое натуральное число "))
number_2 = int(input("ввведите второе натуральное число "))
if number_1 < number_2:
    left_border = number_1
    right_border = number_2
else:
    left_border = number_2
    right_border = number_1
my_list = []
for x in range (left_border, right_border):
    number_3 = 2*x
    total = number_3
    my_list.append(total)
my_list.append(right_border*2)
print (sum(my_list))