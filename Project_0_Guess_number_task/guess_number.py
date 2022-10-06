"""Проект Угадай число
Компьютер загадывает число рандомно и затем угадывает его менее чем за 20 попыток
"""

import numpy as np


def random_predict(number:int=1) -> int:
    """Число загадывается рандомно, затем отгадывается путем поэтапного сокращения интервала

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    number = np.random.randint(1, 101) # загадываем число
    count = 0 # счетчик попыток
    min, max = 1, 101 # задаем первоначальный интервел поиска числа
            
    while True:
        count += 1
        predict_number = (min + max)//2 # угадываемое число, стартуем с середины интервала
        if number == predict_number:
            break  # выход из цикла, число угадано
        elif number > predict_number:
            min = predict_number # сокращаем интервал в большую сторону
        elif number < predict_number:
            max = predict_number # сокращаем интервал в меньшую сторону
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

