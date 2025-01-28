import random

i = 0
my_array = []

while i < 6:
    number = (random.randint(0, 100))
    my_array.append(number)
    i = i+1

print (f"{my_array} \n ")

i =0
while i < 5:
    if ((my_array[i] + my_array[i+1])% 6) != 0 and (my_array[i]*my_array[i+1]) < 1000:
        print (f" это числа {my_array[i]} и {my_array[i+1]}")
    
    i = i +1

