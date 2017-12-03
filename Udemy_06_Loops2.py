names = ['John','Shepard','Jack','Joe']
email_domains = ['gmail','o2','hotmail','yahoo']

for i,j in zip(names, email_domains):  #zip łączy dwa zbiory danych
    print(i + "@" + j + ".com")  #wyswielta john@gmail.com, shepard@o2.com, etc.

