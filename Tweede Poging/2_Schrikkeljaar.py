def checkSchrikkeljaar():
    # pak input value van gebruiker en deel die door 400 
    value = int(input("Voer in getaal: ")) / 400  
    # convert de input /400 in alleen maar decimalen en kijk als die groter is dan 0.0(groter dan 0.0 betekent een float, dus geen schrikkeljaar)
    if value % 1 > 0.0: 
        print("geen schrikkeljaar")
    else:
        print("schrikkeljaar")
if __name__ == "__main__" :
    checkSchrikkeljaar()