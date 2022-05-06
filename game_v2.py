"""Игра: Угадай число!
Компьютер сам загадывает и угадывает числа.
"""

import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно задаем число!

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return count

print(f'Вы угадали число за {random_predict()} попыток')

def score_game(random_predict) -> int:
    """Нахождение среднего числа попыток угадывания загаданного 1000 раз числа

    Args:
        random_predict (_type_): Автоматически загаданное число

    Returns:
        int: среднее значение попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101,size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Среднее число попыток угадывания 1000 загаданных чисел {score}')
    return score
   

# RUN
if __name__ == '__main__':
    score_game(random_predict)   
    
