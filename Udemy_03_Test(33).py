def age_foo(age):
    new_age = float(age)+1
    return new_age

def celcius_to_faren(temp_celc):
    faren = float(temp_celc)*9/5 +32
    return faren

age_prompt = input("What is your age: ")  #Promt dopytuje sie o age i wrzuca do zmiennej age_prompt
print(age_foo(age_prompt))  #Wykonuje funkcje age_foo dla wartosci z promptu
print(celcius_to_faren(-3))

