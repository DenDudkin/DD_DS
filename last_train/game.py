import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100'))
    if predict_number < number:
        print(f'Число должно быть больше!')
    elif predict_number > number:
        print(f'Число должно быть меньше!')
    else:
        print(f'Вы угадали число! Это число ={number} за {count} попыток')
        break       