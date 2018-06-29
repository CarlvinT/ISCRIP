def leesMorseCodes(path):
    with open(path) as f:
        data = f.read().splitlines()

    morseCode = dict()

    for line in data:
        codes = ''
        for i in range(len(line)):
            if i > 1:
                codes += line[i]
        morseCode[line[0]] = codes

    return morseCode


karakterNaarCode = leesMorseCodes('morseCodeFiles/morsecode.txt')

def tekstNaarMorse(zin, karakterNaarCode):
    zin = zin.split()

    morse = ''
    for woord in zin:
        for letter in woord:
            morse += karakterNaarCode[letter.upper()] + ' '

        morse += '/'

    return morse

morse = tekstNaarMorse('SOS Piet', karakterNaarCode)

def morseNaarTekst(morse, karakterNaarCode):
    woorden = morse.split('/')
    #print karakterNaarCode.items()

    tekst = ''
    for word in woorden:
        for letter in word.split():
            for c,m in karakterNaarCode.items():
                if m == letter:
                    tekst += c
        tekst += ' '

    return tekst



#morse2tekst = morseNaarTekst(morse, karakterNaarCode)

def main():
    print morseNaarTekst(morse, karakterNaarCode)

if __name__ == '__main__':
    main()