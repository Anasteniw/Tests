
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def rus_logs():
    for id, location in enumerate(geo_logs):
        if 'Россия' not in list(location.values())[0]:
            del(geo_logs[id])
            print (*geo_logs, sep ='\n')
    return


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
newlist = []
def uniq_ids():
    lst = ids.values()
    for elem in lst:
        for value in elem:
            newlist.append(value)
    print(list(set(newlist)))
    return newlist


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def max_fol():
    rating = max(stats, key = stats.get)
    return rating

