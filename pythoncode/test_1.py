def concatenate_number_five_times(number):
  result_string = str(number)
  for _ in range(4): # 4 итерации, так как начальное число уже есть
    result_string += str(number)
    print(result_string)

# Получаем число от пользователя
try:
  user_input = input("Введите число: ") #Можно вводить и не целое число
  concatenate_number_five_times(user_input)
except ValueError:
  print("Ошибка: Введите число.")