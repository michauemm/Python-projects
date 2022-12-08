First usr inputs how many actions will be taken (n)
next n input lines contain actions like:

add_book - adds book to the library. Input in the form of tuple: ("add", "Pan Tadeusz", "Adam Mickiewicz", 2000)

lend - the library lends book to the reader (only one edition per book, max 3 books)
example input: ("lend", "Jakub Dzikowski", "Quo Vadis")

return - returns book to the library 
input example: ("return", "Jakub Dzikowski", "Quo
Vadis") 

Input example:
 12
(" add ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000)
(" add ", "Quo Vadis ", " Henryk Sienkiewicz ", 2010)
(" add ", " Chatka Puchatka ", " Alan Alexander Milne ", 1998)
(" add ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000)
(" add ", " Chatka Puchatka ", " Alan Alexander Milne ", 2014)
(" borrow ", " Bartek Perkowski ", "Pan Tadeusz ")
(" borrow ", " Bartek Perkowski ", "Pan Tadeusz ")
(" wypozycz ", " Jacek Malyszko ", "Quo Vadis ")
(" wypozycz ", " Bartek Perkowski ", "Quo Vadis ")
(" return ", " Jacek Malyszko ", "Quo Vadis ")
(" borrow ", " Bartek Perkowski ", "Quo Vadis ")
(" return ", " Jacek Malyszko ", "Quo Vadis ")

Output:
True
True
True
True
True
True
False
True
False
True
True
False
