
def calcHotDays(values):
    # Variables voor het checken van de aantal dagen en als er een hittegolf is
    TotalHotDays = 0
    HitteGolfen = False
    # Loop voor elke waarde in values
    for value in values:
        # check als de value hoger is dan 25 anders reset de aantal dagen
        if value >= 25:
            TotalHotDays += 1
        else:
            TotalHotDays = 0
        # check voor het hitte dagen streak
        if TotalHotDays >= 5:
            HitteGolfen = True
    # check voor hitte dag en print antwoord uit
    if HitteGolfen == True:
        print("Hittgolf")
    else:
        print("Geen Hittegolf")


def HitteGolf():
    # Variable voor het looping
    looping = True
    #  Array voor all de waardes die binnen komen 
    values = []
    # Blijf loopen tot dat iets anders dan een float binnen komt
    while looping:
        try:
            x = float(input("enter values: "))
            values.append(x)
            #print(x)
        except:
            calcHotDays(values)
            looping = False

if __name__ == "__main__" :
    HitteGolf()