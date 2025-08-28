# Activity 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def read(self):
        print(f"Reading '{self.title}' by {self.author} 📖")
    
    def info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages")

class Ebook(Book): 
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size
    
    def download(self):
        print(f"Downloading '{self.title}'... File size: {self.file_size}MB 💾")
    
    def read(self):
        print(f"Reading '{self.title}' on your e-reader 📱")



# Activity 2


class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("The bird flies 🕊️")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")







if __name__ == "__main__":
    print("Activity 1 Demo:")
    book1 = Book("1984", "George Orwell", 328)
    ebook1 = Ebook("Python Basics", "Jane Doe", 250, 5)

    book1.read()
    book1.info()

    ebook1.read()       
    ebook1.download()

    print("\n Activity 2 Demo:")
  
    animals = [Dog(), Bird(), Fish()]
    for a in animals:
        a.move() 
