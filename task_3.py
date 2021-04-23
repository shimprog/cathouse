"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company = dict()
company["Мак"] = 100000
company["Бургер"] = 1000
company["Лиаз"] = 1000000
company["Теремок"] = 10000
company["Сашкин Корпарейшен"] = 9999999
company["Зорро"] = 50055


"Сложность O(N log N)"


def best_comp_v1(dictionary):
    dictionary_sort = sorted(dictionary, key=dictionary.get, reverse=True)  # O(N log N)
    dict_fin = dict()   # O(1)
    i = 0   # O(1)
    for key in dictionary_sort:     # O(N)
        dict_fin[key] = dictionary[key]     # O(N)
        i = i + 1   # O(1)
        if i == 3:  # O(1)
            break
    return dict_fin     # O(1)


"Сложность O(N^2)"


def best_comp_v2(dictionary):
    dict_fin = dict()   # O(1)
    dictionary_values = dictionary.values()     # O(1)
    dictionary_values_list = list(dictionary_values)    # O(len(...))
    i = 0   # O(1)
    while i <= 2:   # O(1)
        max_values = max(dictionary_values_list)    # O(N)
        index_max_el = dictionary_values_list.index(max_values)     # O(1)
        for key, values in dictionary.items():  # O(N)
            if values == max_values:    # O(1)
                dict_fin[key] = max_values  # O(1)
        dictionary_values_list.pop(index_max_el)    # O(1)
        i = i + 1   # O(1)

    return dict_fin     # O(1)


print(best_comp_v1(company))
print(best_comp_v2(company))
