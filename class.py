

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  # Using protected for potential subclass access

    def get_summary(self):
        return f"'{self.title}' by {self.author} ({self._pages} pages)"

    def read(self):
        return f"You start reading '{self.title}'..."

    def display_details(self):
        print("--- Book Details ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self._pages}")
        print(f"Summary: {self.get_summary()}")
        print(self.read())
        print("----------------------")


class Ebook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def read(self):
        return f"Opening eBook '{self.title}'... (Size: {self.file_size}MB)"

    def display_details(self):
        super().display_details()
        print(f"File Size: {self.file_size} MB")
        print("----------------------")


class AudioBook(Book):
    def __init__(self, title, author, pages, duration):
        super().__init__(title, author, pages)
        self.duration = duration  # in minutes

    def read(self):
        return f"Now playing audiobook '{self.title}'... Duration: {self.duration} mins"

    def display_details(self):
        super().display_details()
        print(f"Duration: {self.duration} mins")
        print("----------------------")


def get_book_input():
    """Prompts the user for book type and details."""
    book_type = input("Enter the type of book (book, ebook, audiobook): ").lower()
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    pages = int(input("Enter the number of pages: "))

    if book_type == "ebook":
        file_size = float(input("Enter the file size (in MB): "))
        return Ebook(title, author, pages, file_size)
    elif book_type == "audiobook":
        duration = int(input("Enter the duration (in minutes): "))
        return AudioBook(title, author, pages, duration)
    elif book_type == "book":
        return Book(title, author, pages)
    else:
        print("Invalid book type.")
        return None

# Get book input from the user
book_instance = get_book_input()

# Display the details of the created book object (demonstrating polymorphism)
if book_instance:
    book_instance.display_details()

    # Demonstrate polymorphism with the 'read' method
    print("\n--- Reading the Book ---")
    print(book_instance.read())
    print("------------------------")



    class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Mammal(Animal):
    def move(self):
        print(f"{self.name} is walking.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying.")

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"The {self.model} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"The {self.model} is driving. 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"The {self.model} is flying. ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"The {self.model} is sailing. ⛵")

# Create instances of different animals and vehicles
dog = Mammal("Buddy")
salmon = Fish("Finny")
eagle = Bird("Sky")
sedan = Car("Sedan X")
jet = Plane("SuperSonic")
yacht = Boat("Ocean Dream")

# Create a list of these objects
things_that_move = [dog, salmon, eagle, sedan, jet, yacht]

# Iterate through the list and call the move() method on each object
print("--- Actions of different moving things ---")
for thing in things_that_move:
    thing.move()
print("---------------------------------------")

# Demonstrate polymorphism with a function
def make_it_move(movable_object):
    movable_object.move()

print("\n--- Polymorphic behavior through a function ---")
make_it_move(dog)
make_it_move(jet)
print("---------------------------------------------")