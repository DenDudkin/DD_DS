import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        number_predict = np.random.randint(1, 101) #предполагаемое число
        if number_predict == number:
            break
    
    return count

print(f'Количество попыток: {random_predict(67)}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
        угадываем наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = np.mean(count_ls)
    
    return score

print(score_game(random_predict))    


#RUN
if __name__ == '__main__':
    score_game(random_predict)