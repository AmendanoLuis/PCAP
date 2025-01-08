class Book:
    # Constructor

    def __init__(self, title, quantity, author, price):

        self.title = title
        self.quantity = quantity 
        self.author = author
        
        # Encapsulation: private attributes 
        self.__price = price
        self.__discount = None

    # setter method
    def set_discount(self, discount):
        self.__discount = discount
    
    # getter function
    def get_price(self):
        if self.__discount:  # is defined
            return self.__price * (1-self.__discount)
        return self.__price

    # Return a printable representation of the object
    def __repr__(self):
            return f"Titulo:\'{self.title}', Cantidad: {self.quantity}, Autor: {self.author}, Precio: {round(self.get_price(),3)}"
        

        
        
book1 = Book('El Señor de los anillos',30,'J.R.R. Tolkien',22)

print(book1)

print(book1.title)
print(book1.quantity)
print(book1.author)