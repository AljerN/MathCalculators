# (c) 2025 cabarsebongot
#This program solves for the dilution problem
def main ():
    volume_2 = float(input("what is the initial of the solution (L)?"))
    concentration_1 = float(input("what is the initial concentration (g/L) ?"))
    concentration_2 = float(input( "what is the final concentration (g/L) ?"))
    
    
    volume1 = (concentration_2 * volume_2) / concentration_1
    
    print (f"\nSo, you need {volume1} mL of the original sample.")
    
if __name__ == "__main__":
    main()