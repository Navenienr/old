def logics(number_1, number_2):
    if number_1 < number_2:
        left_border = number_1
        right_border = number_2+1
    else:
        left_border = number_2
        right_border = number_1+1
    my_list = []
    for x in range (left_border, right_border):
        if (x % 5) == 0:
            my_list.append(x)
    print (sum(my_list))

number_1 = int(input("ввведите первое натуральное число "))
number_2 = int(input("ввведите второе натуральное число "))
while (number_1-number_2) > 100 or (number_2-number_1) > 100:
    print ("введите 2 числа так, что бы их частное было меньше или равно 100")
    number_1 = int(input("ввведите первое натуральное число "))
    number_2 = int(input("ввведите второе натуральное число "))

logics(number_1, number_2)
