#!!!!!! NIET HELEMAAL WERKEND


def hint(gok,correct):
    #loop door elke letter van de correcte woord
    for index,letter in enumerate(correct):
        #loop door elke letter van het gok 
        for index2,letter2 in enumerate(gok):
            #check als de huidige letter van correct in de gok zit
            if letter in gok:

                # als de letter op de zelfde plek zit, vervand die met hoofdletter
                if index2 == index and letter == letter2:
                    print (letter.capitalize())
                # anders vervang die met kleine letter / doe niks
                else:
                    print(letter)
            # als de huidige letter van correct niet in de gok zit, vervang die met een .
            else:
                correct.replace(letter, ".")
    
    print(correct)
                
                
    
    


    

if __name__ == "__main__" :
    hint("kluis","eruit")