# hand1 = ["3h","Ah","7d","6h","8c","2d","9c","2h","Ks","3s"]
# hand2 = []
# hand3 = ["5h","5d","5s","6c","4d","6d","Jd","4h","10d","Ah"]
def Kings(hand):
    #print("test start")
    size = len(hand)
    availible = [True]*size
    throw = []
    for i in range(size):
        for j in range(i+1, size):
            if availible[i] and availible[j] and hand[i][0] == hand[j][0]:
                availible[i] = False
                availible[j] = False
                throw.append((i, j))
    #             print("throw", hand[i], hand[j])

    # print(throw)
    return throw
# Kings(hand1)
# Kings(hand2)
# Kings(hand3)
