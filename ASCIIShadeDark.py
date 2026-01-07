levels = [
    '▇',
    '▧',
    '@',
    '#',
    '*',
    '+',
    '^',
    '~',
    '-',
    '.',
    ' '
]

def get(level:int):
    return levels[int(level) % len(levels)]