from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Александр', 'Алексей', 'Николай']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result=((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))

print(list(result))
