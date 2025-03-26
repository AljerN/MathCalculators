# (c) 2025 cabarsebongot
#This program solves for the material strength
def main ():
    Force = float(input("Enter force applied(N): "))
    Area = float(input("Enter crossectional area(mm^2) :"))
    
    Conversion = Area * (1/1000000)
    
    σ = Force / Conversion
    
    print(f"So, the stress on the beam is {σ:,.2f} Pa.")
    
if __name__ == "__main__":
    main()