# BMI calculator
logo ='''

  ____  __  __ _____    _____      _            _       _             
 |  _ \|  \/  |_   _|  / ____|    | |          | |     | |            
 | |_) | \  / | | |   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 |  _ <| |\/| | | |   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |_) | |  | |_| |_  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |____/|_|  |_|_____|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                                                                                            
'''
print(logo)

print('You need to enter your "weight" and "height" below.')
print('Choose which unit do u want to use. \n\t!!P.S: Enter only \"1\" or \"2\"!!')
print('Mass unit: \n\t1) Kg & m (Metric units) \n\t2) Lb & In (Imperial units)')

wUnit = input('Enter Chosen units: ')
int_wUnit = int(wUnit)
if int_wUnit == 1:

    kg = input('Enter your weight in \"Kg\": ')
    m  = input('Enter your height in \"Meter\": ')

    ikg = float(kg)
    im = float(m)

    bmi = ikg / (im *im)
    print(f'BMI: {bmi}')

elif int_wUnit == 2:
    lb = input('Enter your weight in \"Lb\"')
    inch = input('Enter your weight in \"Inches\"')

    ilb = float(lb)
    i_inch = float(inch)

    ikg_c = ilb * 0.4536
    im_c = i_inch * 0.025

    bmi2 = ikg_c / (im_c * im_c)
    print(f'BMI: {bmi2}')

else:
    print("Enter 1 or 2!Please try again!")

