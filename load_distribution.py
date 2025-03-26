# (c) 2025 cabarsebongot
#This program solves for the load distribution on a beam
def main ():
    L = float(input("Enter length (m): "))
    w = float(input("Enter load (N/m): "))
    
    F = w * L
    
    print(f"So, the total load acting on the beam is {F:,.2f} N. ")
    
if __name__ == "__main__":
    main()