from random import randrange, choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(a):
    i = 0
    joke = []
    while i < a:
        bonus=f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        joke.append(bonus)
        i += 1
    print(joke)

get_jokes(2)
#функция шутит шутки
