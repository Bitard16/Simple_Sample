import string
from random import seed,randint
datastreans = list(string.ascii_uppercase + string.ascii_lowercase)
 # Simple
print(datastreans)
seed(9)
sample_size = 5
sample = []

for index, element in enumerate(datastreans):
    # Добавляе м элементы до заполения выборки
    if index < sample_size:
        sample.append(element)
    else:
        # Заполнив выборку мы смотрим нужно ли нам еще заменять элементы
        draw = randint(0,index)
        if draw < sample_size:
            sample[draw] = element

print(sample)

