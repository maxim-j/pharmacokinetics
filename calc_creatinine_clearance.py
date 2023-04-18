
print("Cockcroft-Gault formula for creatinine clearance.")

def pt_information():
    """Used to collect initial pt parameters of age, sex and height."""

    while True:
        age = input("Age (yrs): ")
        if age.isdigit():
            age = int(age)
            if age > 0:
                break
            else:
                print("Invalid age.")
        else:
            print("Invalid age.")

    while True:
        sex = input("Sex (M/F): ")
        if sex.upper() == "M" or sex.upper() == "F":
            break
        else:
            print("Invalid sex.")
    
    return age, sex


def pt_height():
    while True:
        height_input = input("Height (in or cm): ")
        if height_input[0].isdigit() and height_input.endswith("in"):
            height_in = int(height_input[:-2])
            return height_in
        elif height_input[0].isdigit() and height_input.endswith("cm"):
            height_cm = int(height_input[:-2])
            height_in = height_cm / 2.54
            return height_in
        else:
            print("Invalid height.")

def get_tdbw():
    """Used to collect dry body weight in kg or lb."""

    while True:
        tdbw_input = input("Dry body weight (kg or lb): ")
        if tdbw_input[0].isdigit() and tdbw_input.endswith("kg"):
            tdbw_kg = float(tdbw_input[:-2])
            return tdbw_kg
        elif tdbw_input[0].isdigit() and tdbw_input.endswith("lb"):
            tdbw_lb = float(tdbw_input[:-2])
            tdbw_kg = tdbw_lb * 0.453592
            return tdbw_kg
        else:
            print("Invalid weight.")

def get_serum_creatinine():
    """Used to collect serum creatinine in mg/dL."""

    while True:
        serum_creatinine = input("Serum creatinine (mg/dL): ")
        if serum_creatinine.isdigit() or (serum_creatinine.count(".") == 1 and serum_creatinine.replace(".", "").isdigit()):
            serum_creatinine = float(serum_creatinine)
            if serum_creatinine > 0.0:
                break
            else:
                print("Invalid serum creatinine.")
        else:
            print("Invalid serum creatinine.")
    return float(serum_creatinine)

def ibw_calc(sex, height_in, tdbw_kg):
    
    height_ft = height_in // 12
    height_inch = height_in % 12
    
    if height_ft >= 5:
        if sex.upper() == "M":
            ibw = 50 + 2.3 * (height_inch)
        else:
            ibw = 45 + 2.3 * (height_inch)
        return ibw
    else:
        ibw = tdbw_kg
        return ibw, height_ft, height_inch

def weight_used_in_calc(tdbw_kg, ibw):
    if tdbw_kg / ibw < 1:
        return tdbw_kg
    elif 1 <= tdbw_kg / ibw <= 1.3:
        return ibw
    else:
        adjbw = ibw + 0.4 * (tdbw_kg - ibw)
        return adjbw

def main():
    age, sex = pt_information()
    height_in = pt_height()
    tdbw_kg = get_tdbw()
    serum_creatinine = get_serum_creatinine()

    ibw = ibw_calc(sex, height_in, tdbw_kg)
    weight_calc = weight_used_in_calc(tdbw_kg, ibw)

    print(f"Age: {age} yo, Sex: {sex}, Ht: {height_in:.0f} in, Wt: {tdbw_kg:.1f} kg, SCr: {serum_creatinine} mg/dL.")

    if sex.upper() == "M":
        creatinine_clearance = ((140 - age) * weight_calc) / (72 * serum_creatinine)
    else:
        creatinine_clearance = (((140 - age) * weight_calc) / (72 * serum_creatinine)) * 0.85

    print(f"Creatinine clearance: {creatinine_clearance:.1f} mg/dL.")
    print(f"Weight used: {weight_calc:.1f} kg")

main()
