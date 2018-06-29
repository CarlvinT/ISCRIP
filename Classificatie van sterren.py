def classificatie(temperatuur, lichtkracht):

    if (lichtkracht < 0.01) and (temperatuur < 30000 and temperatuur > 5000):
        return 'witte dwergen'
    elif (lichtkracht < 0.01) and (temperatuur < 5000 and temperatuur > 3000):
        return 'witte dwergen'
    elif (lichtkracht > 10 and lichtkracht < 100) and (temperatuur < 6000 ):
        return 'reuzen'
    elif (lichtkracht > 100 and lichtkracht < 1000) and (temperatuur < 7500):
        return 'heldere reuzen'
    elif (lichtkracht > 1000 and lichtkracht < 10000):
        return 'superreuzen(b)'
    elif (lichtkracht > 10000):
        return 'superreuzen(a)'
    else:
        return 'hoofdreeks'

def cataloog(filePath):
    # Dictionary Variable // Populating a dictionary: catalog['Key'] = Value || catalog = {'key': value, 'key', value}
    catalog = {}

    # for loop count variable
    count = 0

    # Open and read file
    fileOpen = open(filePath,'r')
    file = fileOpen.read()

    #Clean up file input
    fileLines = file.splitlines()

    for lines in fileLines:
        if count > 1:
            if len(fileLines[count].split()) > 7:
                catalog[fileLines[count].split()[0] + ' ' + fileLines[count].split()[1]+ '  ' + fileLines[count].split()[2]] = float(fileLines[count].split()[4]), float(fileLines[count].split()[5])

            else:
                catalog[fileLines[count].split()[0] + ' ' + fileLines[count].split()[1]] = float(fileLines[count].split()[3]), float(fileLines[count].split()[4])

        count += 1

    return catalog

def klassen(dic):

    stars = cataloog(dic)
    klassenDic = {}

    #Getting Stars and their data ( data = star keys (name) )
    for data in stars:
        classed = classificatie(stars[data][0], stars[data][1])

        if classed in klassenDic:
            #Needs to be fixed
            klassenDic[classed] += data

        else:
            klassenDic[classed] = data


    print klassenDic






def main():
    return klassen('ClassificatieSterFiles/sterren.txt')

if __name__ == '__main__':
    print(main())