import sys


def classification_mapping(classification):
    if classification != '10':
        return classification[0].upper()


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

def grouping(features):
    symbols = list(filter(isSymbol, features))
    numbers = list(filter(isNumber, features))

    minDists = [('-1', sys.maxsize)] * len(numbers)

    cards = [()] * len(numbers)
    for n in range(len(numbers)):
        for s in range(len(symbols)):
            dist = (numbers[n][1] - symbols[s][1]) ** 2 + \
                (numbers[n][2] - symbols[s][2]) ** 2
            if dist < minDists[n][1]:
                minDists[n] = (symbols[s][0], dist)
        cards[n] = (numbers[n][0], minDists[n][0])

    print(set(cards))


grouping(features)
