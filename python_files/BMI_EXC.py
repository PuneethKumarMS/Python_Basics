w=int(input('enter weight in kg: '))
h=float(input('enter height in meter: '))
print(id(w),id(h))
BMI=(w//h**2) # Body Mass Index formula
print(BMI)
print(id(BMI))
