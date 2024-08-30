# Create a class hierarchy for a library system. The base class LibraryItem should have properties like title and author and methods such as checkout() and return_item(). 
# Derive three classes: Book, Magazine, and DVD, each with additional properties and methods specific to their type. 
# Implement method overriding and use the derived classes to perform various library operations.

class Library:
    def __init__(self, title, author):
        self.title = title 
        self.author = author
        self.check_out = False
        
    def checkout(self):
        if not self.check_out:
            self.check_out = True
            print(f"{self.title} has been Checked Out.")
        else:
            print(f"{self.title} is already Checked Out.")

    def return_item(self):
        if self.check_out:
            self.check_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not currently Checked Out.")

class Book(Library):
    def __init__(self, title, author, barcode):
        super().__init__(title, author)
        self.barcode = barcode

    def checkout(self):
        super().checkout()
        print("Please return the Book within 1 Week.")
    
    def return_item(self):
        super().return_item()
        print("Thank you for returning the Book.")
        
class Magazine(Library):
    def __init__(self, title, author, issue_no):
        super().__init__(title, author)
        self.issue_no = issue_no

    def checkout(self):
        super().checkout()
        print("Please return the Magazine within 5 Hours.")

    def return_item(self):
        super().return_item()
        print("Thank you for returning the Magazine.")

class DVD(Library):
    def __init__(self, title, author, director):
        super().__init__(title, author)
        self.director = director

    def checkout(self):
        super().checkout()
        print("Please return the DVD within 2 Days.")
    def return_item(self):
        super().return_item()
        print("Thank you for returning the DVD.")

book1 =Book("Rich Dad Poor Dad", "Robert Kiyosaki", "9780446677455")
mag1 = Magazine("New Yorker ", "Many Authors", 2)
dvd1 = DVD("The Adventures of Robin Hood", "William Keighley", "Michael Curtiz")
mag2 = Magazine("Kenyon Review", "David Baker", 4)

book1.checkout()
mag1.checkout()
dvd1.checkout()
mag2.checkout()

mag1.return_item()
dvd1.return_item()
