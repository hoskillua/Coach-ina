import sys


def isSymbol(variable):
    letters = ['C', 'S', 'D', 'H']
    if (variable[0] in letters):
        return True
    else:
        return False


def isNumber(variable):
    return not isSymbol(variable)


features = [
    ('D', 589, 666),
    ('D', 694, 716),
    ('D', 735, 615),
    ('D', 631, 571),
    ('D', 706, 547),
    ('D', 779, 524),
    ('D', 674, 476),
    ('D', 713, 378),
    ('D', 821, 422),
    ('D', 880, 447),
    ('D', 656, 354),
    ('D', 529, 644),
    ('D', 753, 735),

    ('H', 608, 348),
    ('H', 543, 349),
    ('H', 200, 552),
    ('H', 157, 665),

    ('S', 448, 370),
    ('S', 478, 466),
    ('S', 390, 397),
    ('S', 131, 779),
    ('S', 156, 826),

    ('C', 261, 450),
    ('C', 245, 503),
    ('C', 449, 737),

    ('9', 670, 309),
    ('9', 895, 410),
    ('9', 731, 777),
    ('9', 512, 684),
    ('9', 375, 357),

    ('2', 119, 649),

    ('10', 540, 299),

    ('Q', 113, 824),

    ('K', 214, 471)
]

# features = [
#     ('A', 790, 70),
#     ('A', 810, 330),
#     ('A', 440, 130),
#     ('Q', 290, 179),
#     ('10', 200, 220),
#     ('K', 150, 280),
#     ('J', 135, 340),
#     ('H', 275, 250),
#     ('H', 240, 295),
#     ('D', 245, 355),
#     ('S', 355, 195),
#     ('S', 410, 170),
#     ('C', 465, 155),
#     ('C', 850, 100),
#     ('C', 800, 200),
#     ('C', 750, 310),
# ]

symbols = list(filter(isSymbol, features))
numbers = list(filter(isNumber, features))

minDists = [('-1', sys.maxsize)] * len(numbers)

for n in range(len(numbers)):
    for s in range(len(symbols)):
        dist = (numbers[n][1] - symbols[s][1]) ** 2 + \
            (numbers[n][2] - symbols[s][2]) ** 2
        if dist < minDists[n][1]:
            minDists[n] = (symbols[s][0], dist)
    numbers[n] = (numbers[n][0], minDists[n][0])

print(set(numbers))

#Data = [(A,S),(2,D),(3,S),(4,H),(5,C)]
