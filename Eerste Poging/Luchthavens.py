import math

def leesLuchthavens(bestandsnaam):
    with open(bestandsnaam) as i:
        document = i.read().splitlines()

    luchthavens = {}
    for key in document:
        skey = key.split()

        if len(skey) == 5:
            data = (skey[1],skey[2],skey[3],skey[4])
            luchthavens[skey[0].strip('[').strip(']')] = data
        elif len(skey) == 6:
            data = (float(skey[1]), float(skey[2]), skey[3] + ' '+  skey[4], skey[5])
            luchthavens[skey[0].strip('[').strip(']')] = data

    return luchthavens

luchthavens = leesLuchthavens('LuchthavensFiles/luchthavens.txt')

def afstand(code1, code2, luchthavens):
    R = 6372,795
    b1 = luchthavens[code1][0]
    b2 = luchthavens[code2][0]
    l1 = luchthavens[code1][1]
    l2 = luchthavens[code2][1]

    top = math.sqrt(math.pow(math.cos(b2) * math.sin(math.pow(l1-l2,2)) + (math.cos(b1) *)  ,2))
    print luchthavens[code1]
    print luchthavens[code2]


def main():
    afstand('P60', 'MSN', luchthavens)

if __name__ == '__main__':
    main()
