# hand1 = ["3h", "Ah", "7d", "6h", "8c", "2d", "9c", "2h", "Ks", "3s"]
# hand2 = []
# hand3 = ["5h", "5d", "5s", "6c", "4d", "6d", "Jd", "4h", "10d", "Ah"]

# ground1 = ["5h", "5d", "5s", "6c", "4d", "6d", "Jd", "4h", "10d", "Ah"]
# ground2 = ["5h", "5d"]
# ground3 = ["10c", "5c", "7d", "3h", "4h", "5d", "7c",
#            "Jd", "9h", "10h", "Ah", "Kd", "Ad", "6c", "Qh"]

mapScore = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}
mapSymboltoIndex = {
    "s": 0,
    "h": 1,
    "d": 2,
    "c": 3
}


def HandGroundMatcher(hand, ground):
    #print("test start")
    sizeH = len(hand)
    sizeG = len(ground)
    maxH = [-1, -1, -1, -1]  # s,h,d,c
    maxG = [-1, -1, -1, -1]
    for i in range(sizeH):
        if maxH[mapSymboltoIndex[hand[i][-1]]] == -1:
            maxH[mapSymboltoIndex[hand[i][-1]]] = i
        elif mapScore[hand[maxH[mapSymboltoIndex[hand[i][-1]]]][0:-1]] < mapScore[hand[i][0:-1]]:
            maxH[mapSymboltoIndex[hand[i][-1]]] = i
    for i in range(sizeG):
        if maxG[mapSymboltoIndex[ground[i][-1]]] == -1:
            maxG[mapSymboltoIndex[ground[i][-1]]] = i
        elif mapScore[ground[maxG[mapSymboltoIndex[ground[i][-1]]]][0:-1]] < mapScore[ground[i][0:-1]]:
            maxG[mapSymboltoIndex[ground[i][-1]]] = i
    maxMatch = [-1, -1, 0]  # indexH, indexG, maxTotal
    for i in range(4):
        if maxH[i] > -1 and maxG[i] > -1:
            if mapScore[hand[maxH[i]][0:-1]] + mapScore[ground[maxG[i]][0:-1]] > maxMatch[2]:
                maxMatch = [maxH[i], maxG[i],
                            mapScore[hand[maxH[i]][0:-1]] + mapScore[ground[maxG[i]][0:-1]]]

    if maxMatch[0] == -1 and maxMatch[1] == -1:
        maxMatch = []
    # print(maxMatch)
    return maxMatch


#HandGroundMatcher(hand1, ground1)
