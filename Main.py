from Vehicle import Bike, Car, Scooty

def main():
    Xpulse=Bike("Black",2,5)
    XUV700=Car("Navy Blue", 4, 6)
    Activa=Scooty("White",2, 0)
    
    XUV700.display_details()
    print("\n")
    Xpulse.display_details()
    print("\n")
    Activa.display_details()
    print("\n")
    
if __name__ == "__main__":
    main()
    