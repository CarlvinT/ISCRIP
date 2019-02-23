# opening a file:   file = open(path,'r') (r for read r+ for read and write)
# reading a file:   reading = file.read()
# splitting lines:  reading.splitlines()

# replacing char in strings: input.replace('in string','replace with')

def leesBord():
    path = raw_input('Input file path:')
    file = open(path,'r')
    reading = file.read()
    file.close()
    print (reading.splitlines())

def toonBord():
    input = raw_input('Input Sequence:')
    filtering = input.replace('[','')
    filtering = filtering.replace(']','')
    filtering = filtering.replace(', ','\n')
    filtering = filtering.replace("'",'')
    filtering = filtering.replace(' ','.')
    filtering = filtering.replace('',' ')
    print(filtering)

def winnaar():
    input = raw_input('Input Sequence:')
    filtering = input.replace('[','')
    filtering = filtering.replace(']','')
    filtering = filtering.replace("'",'')
    filtering = filtering.replace(', ','')
    a = filtering.replace(' ','.')

    #Horizontal
    if a[0] == a[1] and a[0] == a[2]:
        print(a[0] + ' wint')
    elif a[3] == a[4] and a[3] == a[5]:
        print(a[3] + ' wint')
    elif a[6] == a[7] and a[6] == a[8]:
        print(a[6] + ' wint')

    #Vertical
    elif a[0] == a[3] and a[0] == a[6]:
        print(a[0] + ' wint')
    elif a[1] == a[4] and a[1] == a[7]:
        print(a[1] + ' wint')
    elif a[2] == a[5] and a[2] == a[8]:
        print(a[2] + ' wint')

    #cross left
    elif a[0] == a[4] and a[0] == a[8]:
        print(a[0] + ' wint')

    #cross right
    elif a[2] == a[4] and a[2] == a[6]:
        print(a[2] + ' wint')

    else:
        print('Gelijk spel')


def main():
    winnaar()

if __name__ == "__main__":
    main()