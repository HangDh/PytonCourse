c = "Here"
c.replace("e", "a")
d = c.replace("e", "a")

print(c)  #prints 'Here' - zmiana nie jest dokonywana na stałe, tylko na kopii
print(d)  #prints 'Hara'

listOfStrings = ["Andrzej", "Kinga"]
listOfStrings.append("AK47") # dodaje element do listy
print(listOfStrings[-1]) #wydrukuje AK47 czyli OSTATNI element z listy

tupleExample = ("Hello", 3, 4) # podobne do listy, ale tego nie można modyfikować

#Dictionaries
listExample = [2,3,4]
dictionaryExample = {"Name":"John", "Surname":"Cena", "Age":22}

print(dictionaryExample["Name"])  # 'John' Pozwala na wybranie na podstawie nazwy, czyli troche jak obiekt??

def divide(a,b): # definiowanie funkcji
    try:
        return a/b
    except ZeroDivisionError:
        print("You are dividing by zero")   # Proste ogarnianie exceptions ;)
    except TypeError:
        print("You are trying to divide strings or other bad shit")

print(divide(1,"b"))  #bad shit
print(divide(2,0))  #dividing by zero
