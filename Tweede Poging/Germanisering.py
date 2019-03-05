def Germanisering():
    #input text van de gebruiker en splits elke woord in een list
    zin = input("Enter text: ").split(" ")
    # lees door hele list met een index nummer per woord
    for index,woord in enumerate(zin): 
        # vervang elke woord in het list met een dat begint met hoofdletter
        zin[index] = woord.capitalize() 
    # print hele list
    print(*zin, sep=" ") 



if __name__ == "__main__" :
    Germanisering()