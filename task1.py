def multiplication_table(n):
    results = []
    for i in range(1, n+1):
        for j in range(1, 10):
            result = i * j
            results.append(f"{i} * {j} = {result}")
    return results

# Пример использования
n = int(input("Введите число n: "))
table_results = multiplication_table(n)

# Теперь вы можете использовать результаты как угодно, например, вывести их на экран
for entry in table_results:
    print(entry)
