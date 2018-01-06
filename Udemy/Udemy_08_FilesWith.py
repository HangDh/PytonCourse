with open("example.txt", "a+") as file:
    file.seek(0)  #przesuwa kursor do pozycji 0 (początek)
    content=file.read()
    file.write("Hiho\n")

#File with od razu zamyka plik, dobre zeby nie bylo blokady na pliku.