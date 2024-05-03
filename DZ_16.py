# ДЗ_2 (16)
# поиск четных элементов списка

list_arr = [num+1 for num in range(20)]

even_numbers = [num for num in list_arr if num % 2 == 0]
print(list_arr)
print(even_numbers)
