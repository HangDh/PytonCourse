import json

#  ładujemy jsona i zamieniamy go w dictionary , teraz możemy wywoływać odpowiednie słowa podając klucz
data = json.load(open('data.json'))

#  drukuje opis czym jest "wool" jako wełna : soft curly hair that forms the fleece of sheep...
print(data["wool"])
