import os
import chardet
import timeit

def read_file(file_path, encoding='utf-8'):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    file_encoding = result['encoding']
    with open(file_path, 'r', encoding=file_encoding) as file:
        return file.read()

def boyer_moore_search(text, pattern): # Алгоритм Боєра-Мура
    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    last_occurrence = {pattern[i]: i for i in range(m)}
    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i += m - min(j, 1 + last_occurrence.get(text[i], -1))
            j = m - 1

    return -1

def kmp_search(text, pattern):  # Алгоритм Кнута-Морріса-Пратта
    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    lps = [0] * m
    j = 0

    compute_lps_array(pattern, m, lps)

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def compute_lps_array(pattern, m, lps):
    len_longest_prefix_suffix = 0
    lps[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[len_longest_prefix_suffix]:
            len_longest_prefix_suffix += 1
            lps[i] = len_longest_prefix_suffix
            i += 1
        else:
            if len_longest_prefix_suffix != 0:
                len_longest_prefix_suffix = lps[len_longest_prefix_suffix - 1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp_search(text, pattern): # Алгоритм Рабіна-Карпа
    m, n = len(pattern), len(text)
    if m == 0 or m > n:
        return -1

    prime = 101  

    pattern_hash = calculate_hash(pattern, m)
    text_hash = calculate_hash(text[:m], m)

    for i in range(n - m):  # Оновлено тут
        if pattern_hash == text_hash and text[i:i + m] == pattern:
            return i

        text_hash = recalculate_hash(text, i, i + m, text_hash, m, prime)

    return -1

def calculate_hash(substring, length):
    prime = 101
    hash_value = 0
    for char in substring:
        hash_value = (hash_value * prime + ord(char)) % length
    return hash_value

def recalculate_hash(text, old_index, new_index, old_hash, pattern_length, prime):
    new_hash = (old_hash - ord(text[old_index])) // prime
    new_hash = (new_hash + ord(text[new_index]) * pow(prime, pattern_length - 1)) % pattern_length
    return new_hash

def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=100)

# Зчитуємо тексти з файлів
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

