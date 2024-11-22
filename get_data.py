def get_dog(name):
    # return dogs[name][0], dogs[name][1], dogs[name][2]
    return dogs[name][1], dogs[name][2]

def get_cat(name):
    return cats[name][1], cats[name][2]

def get_dogs_name(pos, step):
    # global i
    # res = i
    pos += step
    if step > 0:
        if pos == len(dogs_names):
            pos = 0
    if step < 0:
        if pos < 0:
            pos = len(dogs_names) - 1
    # else:
    #     pass
    # print(i)
    print(pos)
    print(dogs_names[pos])
    return dogs_names[pos], pos

def get_cats_name(pos, step):
    pos += step
    if step > 0:
        if pos == len(cats_names):
            pos = 0
    if step < 0:
        if pos < 0:
            pos = len(cats_names) - 1
    # else:
    #     pass
    # print(i)
    print(cats_names[pos])
    return cats_names[pos], pos

dogs = {}
i = 0
dog = ['Груша', 'pets_data/images/собака Груша.jpg', 'Собака Груша\nГруше всего 8 месяцев.\n'
                       'Эта очаровательная рыжая девчонка покоряет с первого взгляда- веселая, ласковая, '
                       'невероятная оптимистка, ну как в такую не влюбиться ? Груша абсолютно открытый и '
                       'доверчивый подросток, любит весь мир вокруг и верит, что впереди только радость. '
                       'Очень любит обниматься, никогда не проявляет агрессии, нежная до невозможности, '
                       'с радостью общается с другими собаками, так что готова стать и вторым питомцем в семье.']
dogs[dog[0]] = dog
dog = ['Арчи', 'pets_data/images/пёс Арчи.jpg', 'Пёс Арчи']
dogs[dog[0]] = dog
dog = ['Шарик', 'pets_data/images/пёс Шарик.jpeg', 'Пес Шарик дружелюбный и любопытный']
dogs[dog[0]] = dog

dogs_names = list(dogs.keys())
print(dogs_names)


cats = {}
i = 0
cat = ['Мура', 'pets_data/images/кошка Мура.jpg', 'Кошка Мура']
cats[cat[0]] = cat
cat = ['Силя', 'pets_data/images/кот Силя.jpg', 'Кот Силя']
cats[cat[0]] = cat
cat = ['Софа', 'pets_data/images/кошка Софа.jpg', 'Кошка Софа']
cats[cat[0]] = cat

cats_names = list(cats.keys())
print(cats_names)