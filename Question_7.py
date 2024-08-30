#  Develop a class SecureDatabase that uses encapsulation to hide its data storage (e.g., a list of records). 
#  The class should provide methods to add, remove, and find records, but the underlying data structure should not be accessible from outside the class. 
#  Use abstraction to define an interface for a generic Database class and implement SecureDatabase as a concrete class.

class SecureDatabase:
    def __init__(self, records):
        self.__records = records
        
    def add_record(self, record):
            self.__records.append(record)
            print(f"{record} added to the Records.")
        
    def remove_record(self, record):
        if record in self.__records:
            self.__records.remove(record)
            print(f"{record} removed from the Records")
        else :
            print(f"{record} is not in the Records.")
        
    def find_record(self, record):
        if record in self.__records:
            print(f"{record} is in Records.")
        else:
            print(f"{record} not found!")
        pass
    # def display(self):
    #     print(f"{self.__records}")


database1 = SecureDatabase([59, 68, 98, 234, 3453, 4564, 23435, 98934])
# database1.display()
database1.add_record(254)
# database1.display()
database1.remove_record(98)
database1.remove_record(99)
# database1.display()
database1.find_record(4564)
database1.find_record(768)
