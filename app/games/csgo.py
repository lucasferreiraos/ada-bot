from random import shuffle


def ban_map_md1(map_name):
    maps = [
        'Dust2',
        'Inferno',
        'Mirage',
        'Nuke',
        'Overpass',
        'Train',
        'Vertigo',
    ]

    if len(maps) == 1:
        return map_name
    elif map_name in maps:
        maps.remove(map_name)
        return map_name


def ban_map_md3(map_name):
    maps = [
        'Dust2',
        'Inferno',
        'Mirage',
        'Nuke',
        'Overpass',
        'Train',
        'Vertigo',
    ]

    if len(maps) == 3:
        shuffle(maps)
        return maps
    elif map_name in maps:
        maps.remove(map_name)
        return map_name


def ban_map_md5(map_name):
    maps = [
        'Dust2',
        'Inferno',
        'Mirage',
        'Nuke',
        'Overpass',
        'Train',
        'Vertigo',
    ]

    if len(maps) == 5:
        shuffle(maps)
        return maps
    elif map_name in maps:
        maps.remove(map_name)
        return map_name
