import os 
import växlare
    
def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n\t-växlare-\n")

    pris = input ("\tmata in pris på varan i kr:")
    inbet = input ("\tinbetalt belopp i kr ")

    #anropar växlings funktionen

    exChangeNow(int(pris), int(inbet))
    #definerar växlings funktion som skriver ut växling

def exChangeNow(priset, inbetalning):
    #print("test")
    
    if (priset > inbetalning):
        print("förlite pengar!")

    else:
        vaxel_tillbaka_dictionary = växlare.get_exchange_dict(inbetalning, priset)
        

main()