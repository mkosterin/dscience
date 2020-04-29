import random
start = 1  # basic rule, min possible number
finish = 100 # basic rule, max possible number
games_count = 1000 # how many times we will game
kinds = 4 # how many different ways to guess a number. Must be the same in guess function

class Number:
    #This class can generate a number a help you to guess it. 
    #Also it counts how many attempt you spend to guess the number.
    __number = 1
    __count = 0
    def __init__(self):
        self.__number = random.randint(start, finish)

    def show_a_number(self): # Only for debug reasons
        return self.__number
    
    def reset_the_counter(self):
        self.__count = 0
        
    def attempt(self, val=int):
        self.__count += 1
        if val > self.__number:
            return 'too big'
        elif val < self.__number:
            return 'too little'
        else:
            how_many = self.__count
            self.reset_the_counter() # reset the counter before trying next way
            return how_many
            

def guess(a: Number, kind=3):
    # This function guess the number using different methods (kind=)
    if kind == 0:
        # Primitive. Try to guess from 1 to 100, we analyze only one response, when we guess the number
        for variant in range(start, finish + 1):
            result = a.attempt(variant)
            if type(result)  == int:
                break
        return variant, result, 'Перебор от {} до {}, без учета подсказок'.format(start, finish)
    elif kind == 1:
        # Primitive. Try to guess from 100 to 1, we analyze only one response, when we guess the number
        for variant in range(finish, start - 1, -1):
            result = a.attempt(variant)
            if type(result)  == int:
                break
        return variant, result, 'Перебор от {} до {}, без учета подсказок'.format(finish, start)
    elif kind == 2:
        # It checks answers and crossout the half each time
        st = start
        fin = finish + 1
        while True:
            variant = (fin + st)//2
            result = a.attempt(variant)
            if type(result) == int:
                break
            elif result == 'too big':
                fin = variant
            elif result == 'too little':
                st = variant
        return variant, result, 'Перебор делением на 2, с учетом подсказок'
    elif kind == 3:
        # It checks answers and crossout the random part each time
        st = start
        fin = finish + 1
        while True:
            variant = random.randint(st, fin)
            result = a.attempt(variant)
            if type(result) == int:
                break
            elif result == 'too big':
                fin = variant
            elif result == 'too little':
                st = variant
        return variant, result, 'Перебор делением на случайное число, с учетом подсказок'
            
print('Исходные данные:')
print('Диапазон от {} до {}'.format(start, finish))
print('Играем {} раз'.format(games_count))

numbers = [Number() for game_count in range(games_count)] # generate list of objects
medium_counts = []
for kind in range(kinds):
    for number in numbers:
        value, attempt, descr = guess(number, kind)
        medium_counts.append(attempt)
    medium = round(sum(medium_counts)/len(medium_counts))
    print('{} попытка(ок) в среднем алгоритмом "{}"'.format(medium, descr))
    medium_counts.clear()
