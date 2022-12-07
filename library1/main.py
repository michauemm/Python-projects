class Library:

    def __init__(self):
        self.edition_list = []
        self.occurance_list = []

    def add_edition(self, title, author):
        book = Book(title, author)
        self.edition_list.append(book)

    def count_occurance(self):
        for element in self.edition_list:
            count_el = str(self.edition_list).count(str(element))
            string = str(element,)
            self.occurance_list.append(f"{string}{count_el})")
        final_list = list(set(self.occurance_list))
        for element in final_list:
            print(element)

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"('{self.title.strip()}','{self.author.strip()}',"

MyLib = Library()
list_input = []

n = int(input())
for i in range(n):
    x = eval(input())
    list_input.append(x)
for element in list_input:
    x = eval(str(element))
    title = element[0]
    author = element[1]
    MyLib.add_edition(title, author)
MyLib.count_occurance()



