def calculate_dosage():
    print("Drug Dosage Calculator")
    print("----------------------")
    
    try:
        weight = float(input("Enter patient weight in kg: "))
        dose_per_kg = float(input("Enter drug dose in mg/kg: "))
        
        if weight <= 0 or dose_per_kg <= 0:
            print("Weight and dose must be positive numbers.")
            return
        
        total_dose = weight * dose_per_kg
        print(f"\nTotal dosage = {total_dose:.2f} mg")
    
    except ValueError:
        print("Please enter valid numeric inputs.")

calculate_dosage()
