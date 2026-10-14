#Actividad 5


# Creamos la clase Book
class Book:

    # Creamos el constructor
    def __init__(self, title, num_pages):

        # Guardamos el título
        self.title = title

        # Guardamos el número de páginas
        self.num_pages = num_pages

    # Este método sirve para mostrar el libro
    def __str__(self):

        # Regresamos el título y las páginas
        return "Book: " + self.title + ", Pages: " + str(self.num_pages)

    # Este método sirve para saber cuántas páginas tiene
    def __len__(self):

        # Regresamos el número de páginas
        return self.num_pages


# Creamos un libro
book = Book("Libro Vaquero", 200)

book2: Book = Book("Cañitas", 115)

# Mostramos el libro
print(book)

print(book2)

# Mostramos el número de páginas
print(len(book))

print(len(book2))