import sys
import csv
import os

class Library():
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def book(self):
        print(self.name, self.author, self.year)

b1 = 'Alice in the Wonderland -', 1865, '- Louis Carrol'
b2 = 'Harry Potter and Philosophers Stone -', 1997, '- J.K.Rowling'
b3 = 'Master and Margarita -', 1940, '- Mikhail Bulgakov'

print('You have entered the library')
while True:
    print('1. Bible\n2. Search\n3. Add a new book\n4. Delete a book\n5. Exit')
    choice = int(input())
    if choice == 1:
            print(b1)
            print(b2)
            print(b3)

    elif choice == 2:
        while True:
            found = int(input('1. Book name search\n2. Release date search\n3. Author name search\n'))
            if found == 1:
                choice2 = input('Input book name:')
                if choice2 == 'Alice in the Wonderland':
                    print('Alice in the Wonderland -', 1865, '- Louis Carrol')
                elif choice2 == 'Master and Margarita':
                    print('Master and Margarita -', 1940, '- Mikhail Bulgakov')
                elif choice2 == 'Harry Potter and Philosophers Stone':
                    print('Harry Potter and Philosophers Stone -', 1997, '- J.K.Rowling')
                else:
                    print('There is no such book')
            elif found == 2:
                choice2 = input('Input release date:')
                if choice2 == '1865':
                    print('Alice in the Wonderland -', 1865, '- Louis Carrol')
                elif choice2 == '1940':
                    print('Master and Margarita -', 1940, '- Mikhail Bulgakov')
                elif choice2 == '1997':
                    print('Harry Potter and Philosophers Stone -', 1997, '- J.K.Rowling')
                else:
                    print('There is no such book')
            elif found == 3:
                choice2 = input('Input book author:')
                if choice2 == 'J.K.Rowling':
                    print('Harry Potter and Philosophers Stone -', 1997, '- J.K.Rowling')
                elif choice2 == 'Mikhail Bulgakov':
                    print('Master and Margarita -', 1940, '- Mikhail Bulgakov')
                elif choice2 == 'Louis Carrol':
                    print('Alice in the Wonderland -', 1865, '- Louis Carrol')
                else:
                    print('There is no such bookт')
    elif choice == 3:
        print('Add a new book')
        filename = input()
        print('A new book was added')
    elif choice == 4:
        os.remove('C:\pythonProject\\text.txt')
    elif choice == 5:
        break