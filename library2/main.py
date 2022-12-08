class Library:
    def __init__(self):
        self.edition_list = []
        self.book_list = []
        self.readers_list = []
        self.score = []


    def available(self, title):
        list = []
        for element in self.edition_list:
            if title == element.title and element.borrowed == False:
                list.append(element)
        if len(list) >= 1:
            return list
        else:
            return False

    def borrow(self, reader, title):
        for element in self.readers_list:
            if reader in str(element):
                if element.borrowed_count >= 3:
                    self.score.append("False")
                    return

                for book in element.list_borrowed:
                    if title in str(book):
                        self.score.append("False")
                        return

                dostep = self.available(title)
                if dostep == False:
                    self.score.append("False")
                    return
                element.list_borrowed.append(dostep.pop())
                element.list_borrowed[-1].borrowed = True
                element.borrowed_count += 1
                self.score.append("True")
            else:
                pass

    def return_book(self, reader, title):
        for element in self.readers_list:
            if reader in str(element):
                if title in str(element.list_borrowed):
                    for el in element.list_borrowed:
                        if title in str(el):
                            el.borrowed = False
                            element.borrowed_count -= 1
                            element.list_borrowed.remove(el)
                            self.score.append("True")
                        else:
                            pass

                else:
                    self.score.append("False")
            else:
                pass

    def add_book_edition(self, title, autor, year):
        book = Book(title, autor)
        edition = Edition(title, year)
        if book.title not in self.book_list:
            self.book_list.append(book.title)
        self.edition_list.append(edition)
        self.score.append("True")
        return

class Edition:

    def __init__(self, title, year, borrowed = False):
        self.title = title
        self.year = int(year)
        self.borrowed = borrowed

    def __repr__(self):
        if self.borrowed == False:
            return f"{self.title} {self.year}, dostępne"
        else:
            return f"{self.title} {self.year,}, wypożyczone"

class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor

    def __repr__(self):
        return f"{self.title, self.autor}"

class Reader:

    def __init__(self, name, borrowed_count = 0):
        self.name = name
        self.borrowed_count = borrowed_count
        self.list_borrowed = []

    def __repr__(self):
        return f"{self.name}"

def main():
    MyLib = Library()

    n = int(input())
    lista_inpt = []
    temp =[]
    z = 0
    for i in range(n):
        x = input()
        lista_inpt.append(x)
    for el in lista_inpt:
        x = eval(str(el))
        if "wypozycz" in str(x[0]):
            reader = x[1]
            temp.append(reader)
    b = list(set(temp))
    for el in b:
        MyLib.readers_list.append(Reader(el))

    for el in lista_inpt:
        x = eval(str(el))
        if "add" in str(x[0]):
            title = x[1]
            autor = x[2]
            year = x[3]
            MyLib.add_book_edition(title, autor, year)

        elif "borrow" in str(x[0]):
            reader = x[1]
            title = x[2]
            MyLib.borrow(reader, title)

        elif "return" in str(x[0]):
            reader = x[1]
            title = x[2]
            MyLib.return_book(reader, title)

    for el in MyLib.score:
        print(el)
main()



