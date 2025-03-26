# (c) 2025 cabarsebongot
#This program solves for the concrete volume
def main ():
    L = float(input("Enter length (m): "))
    W = float(input("Enter width (m): "))
    D = float(input("Enter depth (m): "))
    
    V = L*W*D
    
    print(f"So, you need {V:,.2f} cubic meters of concrete.")
    
if __name__ == "__main__":
    main()