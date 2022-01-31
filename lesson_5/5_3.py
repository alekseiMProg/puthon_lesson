from itertools import zip_longest


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Алексей', 'Федор', 'Егор', 'Григорий'
]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


if len(tutors) > len(klasses):
    name_klass = ((name, klass) for name, klass in zip_longest(tutors, klasses, fillvalue=None))
else:
    name_klass = ((name, klass) for name, klass in zip(tutors, klasses))

print(type(name_klass), *name_klass)