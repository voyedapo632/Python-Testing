levels = [
    '▇',
    '▧',
    '@',
    '#',
    '^',
    '*',
    '.',
    ' '
]

def get(level:int):
    return levels[level % len(levels)]