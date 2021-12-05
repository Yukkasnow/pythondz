def translate(word):
    for key, val in words.items():
        answer = word
        if answer == key:
            print(val)
            break
        if answer[1:]==key[1:]:
            print(val.title())
            break

    if word[1:] != key[1:]:
        print(None)


words = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'

}

translate(input('Введите число коротрое хотите перевести: '))

