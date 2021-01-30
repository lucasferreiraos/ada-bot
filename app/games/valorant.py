from random import shuffle


def ban_map_md1(map_name):
    maps = [
        'ascent',
        'bind',
        'haven',
        'icebox',
        'split'
    ]

    if len(maps) == 1:
        return map_name
    elif map_name in maps:
        maps.remove(map_name)
        return map_name


def ban_map_md3(map_name):
    maps = [
        'ascent',
        'bind',
        'haven',
        'icebox',
        'split'
    ]

    if len(maps) == 3:
        shuffle(maps)
        return maps
    elif map_name in maps:
        maps.remove(map_name)
        return map_name
