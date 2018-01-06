def currency_converter(rate, euros):
    dollars = euros*rate
    return dollars

emails = ['me@gmail.com', 'you@hotmail.com', 'we@gmail.com']

for item in emails:
    if 'gmail' in item:
        print(item)

mylist = [1,2,3,4,5]

for number in mylist:
    print(number)

for number in mylist[-3:]:
    print(number)

r = input("Enter rate: ")
e = input("Enter euros: ")

print(currency_converter(float(r), float(e)))

password = ''
while password != 'python':
    password=input("Enter password: ")
    if password == 'python':
        print("Access granted!")
    else:
        print("Access denied!")

