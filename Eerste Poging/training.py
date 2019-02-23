import math
def gemiddelde(values):
    total = 0.0
    amount = 0

    for item in values:
        if item != None:
            total += item
            amount += 1

    if total > 0.0:
        gem = float(total / amount)
        return gem
    else:
        return None


def gegevensbank(bestand):
    with open(bestand) as f:
        data = f.read().splitlines()
        landen = {}
        for land in data:
            w = land.split('\t')
            naam = w[1]
            waarden = w[2:]

            for i, waarde in enumerate(waarden):
                if waarde:
                    waarden[i] = int(waarde)
                else:
                    waarden[i] = None
            landen[naam] = waarden
        return landen



data = gegevensbank('Files/ohi.txt')

def oceanHealthIndex(land, data):
    data = data[land]
    print data


def main():
    print data
    numbers = [3, None, None, 7, None, 6, 11]
    for item in numbers:
        if None in numbers:
         numbers.remove(None)
    print float(sum(numbers)) / len(numbers)
    #print float(sum(numbers)/len(numbers))

if __name__ == '__main__':
    main()