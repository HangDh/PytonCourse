import json

data = json.load(open("dict\data.json"))

def translate(word):
    if word in data:
        return data[word]

word = input("Enter word: ")

print(translate(word))
