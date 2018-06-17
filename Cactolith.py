
def lettergrepen(input):
    #input = raw_input('Enter Text: ')

    #Set chars to look for
    output = 0
    filters = ['a','e','i','o','u','y','A','E','I','O','U','Y']

    #count total chars that are equals to the filter
    for item in filters:
        output = output + input.count(item)

    return output

def statistieken():
    #Variables
    totalWords = 0
    totalSentences = 0
    totalComplexWords = 0


    #Opening  and Reading file
    path = raw_input('input path:')
    opening = open(path,'r')
    file = opening.read()

    #Splitting the words in the file and counting them
    words = file.split()

    for word in words:
        totalWords += 1


    #getting complex words
    for word in words:
        if lettergrepen(word) > 3:
            totalComplexWords += 1

    #counting sentencs
    totalSentences = file.count('.')

    # printing the words
    statisiek = (totalSentences, totalWords, totalComplexWords)
    return statisiek


def gunningfog():
    #variables
    firstHalf = 0.0
    secondHalf = 0.0
    answer = 0.0

    #getting values
    values = statistieken()
    woorden = float(values[1])
    zinnen = float(values[0])
    complexewoorden = float(values[2])


    #Calculation
    firstHalf = float (woorden / zinnen +100)
    secondHalf = float(complexewoorden / woorden)
    answer = firstHalf * secondHalf * 0.4

    return answer



def main():
    print(gunningfog())


if __name__ == '__main__':
    main()