def age_foo(age):
    new_age = age+1
    return new_age

def celcius_to_faren(temp_celc):
    if temp_celc < -273.15:
        return "That temperature doesn't make sense!"
    else:
        faren = float(temp_celc)*9/5 +32
    return faren

print(celcius_to_faren(-3))

#Dobra zasada - utrzymywać funkcje tak proste jak to możliwe?
age_prompt = int(input("What is your age: "))  #Promt dopytuje sie o age i wrzuca do zmiennej age_prompt
if age_prompt < 150:
    print(age_foo(age_prompt))  #Wykonuje funkcje age_foo dla wartosci z promptu
else:
    print("How is that even possible?")

temperatures=[10,-20,-289,100]

for temp in temperatures:
    print(celcius_to_faren(temp))




