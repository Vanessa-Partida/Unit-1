# This is for lesson 2 in unit 2
def miles_to_km(miles:float)->float:
    """This program converts given miles
    into kilometers. There are 1.61 km in
    a mile.
    
    Parameters
    ----------
    miles:float number of miles
    
    Return
    ------
    float number of kilometers """

    return 1.61*miles

def km_to_feet(km:float)->float:
    return 3280.84*km

# exceptions that could occur: valueerror, typeerror
while True:
    try:
        num_miles = float(input("Enter the number of miles: "))
        num_km = miles_to_km(num_miles)
        print(f"{num_miles:.2f} miles is {num_km:.2f} km.") 
        #.2f rounds to two decimal places
        num_feet = km_to_feet(num_km)
        print(f"{num_km:.2f} km is {num_feet:.2f} feet.")
        break
    except (ValueError,TypeError):
        print("You must enter a number.")
