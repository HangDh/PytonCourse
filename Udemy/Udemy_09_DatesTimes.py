import datetime
import time


def create_file(filename):
    # This function creates an empty file
    with open(filename.strftime("%A-%Y-%m-%d") + ".txt", "w") as file:
        file.write("")  # writing empty string


print(datetime.datetime.now())  # wyświetla bieżącą datę
print(datetime.datetime(2022, 5, 13, 11, 0, 0, 0))  # wyświetla date i czas jak w nawiasach (2022-05-13 11:00:00)

now = datetime.datetime.now()
anniv = datetime.datetime(2018, 9, 16, 0, 0, 0, 0)

delta = anniv - now
print(delta)  # Zawsze pozniejsza data pierwsza ;) jak normalne odejmowanie (tu akurat czas do rocznicy ;D)
print(delta.days)  # Same dni

create_file(now)

strNow = now.strftime("%A-%Y-%m-%d")  # Konwertuje datę na stringa - http://strftime.org/
print(strNow)

after = now + datetime.timedelta(days=2)
print(after)

timeList = []

for i in range(3):
    timeList.append(datetime.datetime.now())
    time.sleep(2.5)  # do usypiania wątków
    print(datetime.datetime.now())
