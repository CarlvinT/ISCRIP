#!!!!!! NIET HELEMAAL WERKEND

# 1 sol  
# 24 uren = 86400 seconden
# 39 minuten = 2340 seconden
# 35 seconden 
# 0.244 seconden 
# Total =  88775,244 seconden  


def calculateSol():
    sol = int(input("Invoer aantaal sol: "))
    seconden = sol * 88775.244
    print ("Aantal dagen: {}".format(seconden/86400))
    
if __name__ == "__main__" :
    calculateSol()

