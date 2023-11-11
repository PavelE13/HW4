import numpy as np # включаем поддержку высокоуровневых математических функций, предназначенных для работы с массивами


def pearson_correlation(x, y): # Функция расчета кореляции Пирсона
    n = len(x)
    m_x = sum(x) / n # Расчитываем среднее значение выборок 1 массива (среднее).
    m_y = sum(y) / n # Расчитываем среднее значение выборок 2 массива (среднее).
    divident = sum((x[i] - m_x) * (y[i] - m_y) for i in range(n)) # Рассчитываем числитель выражения Пирсона
    divider = np.sqrt(sum((x[i] - m_x)**2 for i in range(n))) * np.sqrt(sum((y[i] - m_y)**2 for i in range(n))) # Рассчитываем знаменатель выражения Пирсона
    return divident / divider


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Пример
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 4, 5, 6]
    print(f"Корреляция Пирсона для: \n массива {x} и \n массива {y} равна {pearson_correlation(x, y)} что говорит о тесной связи величин массивов (1 (100%) - полное совпадение величин массивов).")

