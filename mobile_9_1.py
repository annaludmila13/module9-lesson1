def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все функции из *functions
    for func in functions:
        # Вызываем текущую функцию с аргументом int_list
        result = func(int_list)

        # Записываем результат в словарь под ключом имени функции
        results[func.__name__] = result

    # Возвращаем заполненный словарь
    return results
# Пример 1: использование функций max и min
result_1 = apply_all_func([6, 20, 15, 9], max, min)
print(result_1)

# Пример 2: использование функций len, sum и sorted
result_2 = apply_all_func([6, 20, 15, 9], len, sum, sorted)
print(result_2)

