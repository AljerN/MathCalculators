# (c) 2025 cabarsebongot
#This program solves for the slope of the road
def main ():
    R1 = float(input("Enter rise (m): "))
    R2 = float(input("Enter run (m): "))
    
    S = (R1 / R2) * 100
    
    print(f": So, the slope of the road is {S:,.2f}%. ")
    
if __name__ == "__main__":
    main()