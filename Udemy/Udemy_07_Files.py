file = open("example.txt", 'r')  #wczytanie pliku

print(type(file))

content = file.readlines() #Wcztytuje linie po linii (readline wczytuje jedna linie)
print(content)

for line in content:
    print(line)

content = [i.rstrip("\n") for i in content]
print(content)

file.close()  # zamkniecie dostepu z Pythona

file = open("examplewrite.txt", 'w') #utworzenie pliku do zapisu
file.write("Linija 1\n")

numbers = [1,2,3,4]
for n in numbers:
    file.write(str(n)+"\n")

file.close()  # zamkniecie dostepu z Pythona

file.open("examplewrite.txt", 'a') #Append - dodawanie tekstu, nie pisanie od nowa
file.write("Hello\n")  # teraz działa jako append, nie jako write.

# r - read, r+ - read+write, w - write, w+ write+read, overwrite file if exists, a - append, a+ append + read (pointer on the end of file)