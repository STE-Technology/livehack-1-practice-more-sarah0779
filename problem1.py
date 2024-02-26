"""This program determines the atomospheric pressure 
    where water begins to boil from inputed temperature"""

#get temperautre from user
temperature=int(input("Enter the temperature: "))

#calculate atmospheric pressure
atmospheric_pressure = 5 * temperature - 400

#print the result
print(atmospheric_pressure)