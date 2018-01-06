import datetime

print(datetime.datetime.now()) #wyświetla bieżącą datę
print(datetime.datetime(2022,5,13,11,0,0,0)) #wyświetla date i czas jak w nawiasach (2022-05-13 11:00:00)

now = datetime.datetime.now()
anniv = datetime.datetime(2018,9,16,0,0,0,0)

delta = anniv - now
print(delta) #Zawsze pozniejsza data pierwsza ;) jak normalne odejmowanie (tu akurat czas do rocznicy ;D)
print(delta.days) #Same dni

#Lecture 71_6:52
