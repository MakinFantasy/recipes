DATA = {
    'omlet': {
        'яйца, шт': '2',
        'молоко, л': '0.1',
        'соль, ч.л.': '0.5',
    },
    'pasta': {
        'макароны, г': '0.3',
        'сыр, г': '0.05',
    },
    'buter': {
        'хлеб, ломтик': '1',
        'колбаса, ломтик': '1',
        'сыр, ломтик': '1',
        'помидор, ломтик': '1',
    },
    # можете добавить свои рецепты ;)
}

omlet = DATA['omlet']
pasta = DATA['pasta']
buter = DATA['buter']

some_str = str()
for i in omlet:
    try:
        value = int(omlet.get(i))
        value = str(value * 4)
        some_str = some_str + i.title() + " " + value + "; "

    except ValueError:
        value = float(omlet.get(i))
        value = str(value * 4)
        some_str = some_str + i.title() + " " + value + "; "
print(some_str)