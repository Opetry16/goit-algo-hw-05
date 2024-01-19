import timeit

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def boyer_moore_search(text, pattern):
    # Реалізуйте алгоритм Боєра-Мура тут
    pass

def kmp_search(text, pattern):
    # Реалізуйте алгоритм Кнута-Морріса-Пратта тут
    pass

def rabin_karp_search(text, pattern):
    # Реалізуйте алгоритм Рабіна-Карпа тут
    pass

def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=100)

# Зчитуємо тексти з файлів
def read_file(file_path):
    with open(file_path, 'r', encoding='cp1251') as file:
        return file.read()
    
article1 = read_file(r'C:\Users\Олег\Desktop\GOIT\Projects\Repositories\Tier1.Basic Alg.-Data Str\goit-algo-hw-05\goit-algo-hw-05\Exercise3\article1.txt')
article2 = read_file(r'C:\Users\Олег\Desktop\GOIT\Projects\Repositories\Tier1.Basic Alg.-Data Str\goit-algo-hw-05\goit-algo-hw-05\Exercise3\article2.txt')


# Задаємо підрядки для пошуку (існуючий та вигаданий)
existing_pattern = 'your_existing_pattern_here'
fictional_pattern = 'your_fictional_pattern_here'

# Вимірюємо час для кожного алгоритму та тексту
boyer_moore_time_article1 = measure_time(boyer_moore_search, article1, existing_pattern)
kmp_time_article1 = measure_time(kmp_search, article1, existing_pattern)
rabin_karp_time_article1 = measure_time(rabin_karp_search, article1, existing_pattern)

boyer_moore_time_article2 = measure_time(boyer_moore_search, article2, existing_pattern)
kmp_time_article2 = measure_time(kmp_search, article2, existing_pattern)
rabin_karp_time_article2 = measure_time(rabin_karp_search, article2, existing_pattern)

# Виводимо результати для існуючого підрядка
print("Час для алгоритму Боєра-Мура (стаття 1):", boyer_moore_time_article1)
print("Час для алгоритму Кнута-Морріса-Пратта (стаття 1):", kmp_time_article1)
print("Час для алгоритму Рабіна-Карпа (стаття 1):", rabin_karp_time_article1)

print("Час для алгоритму Боєра-Мура (стаття 2):", boyer_moore_time_article2)
print("Час для алгоритму Кнута-Морріса-Пратта (стаття 2):", kmp_time_article2)
print("Час для алгоритму Рабіна-Карпа (стаття 2):", rabin_karp_time_article2)
