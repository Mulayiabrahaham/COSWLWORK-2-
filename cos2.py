from datetime import datetime
import time

print("MULAYI CONRAD ABRAHAM")

# Input name
name = input("Please Enter Your name: ")
print(f"Hello {name.upper()}, Greetings from Group E.")

# Input and validate age
while True:
    try:
        age = int(input("How old are you?: "))
        break
    except ValueError:
        print("Value error: invalid entry, enter a valid number.")

# Calculate year of birth
current_year = datetime.now().year
year_of_birth = current_year - age
print(f"You were born in {year_of_birth}\n")

# Favorite number logic
while True:
    try:
        fav_number = int(input(f"What is your favorite number, {name.upper()}?: "))
        print(f"{fav_number} is an amazing favorite number.")
        if fav_number % 2 == 0:
            print("And guess what, it's an even number.")
            if fav_number > 10:
                print("It's also greater than 10.\n")
            elif fav_number == 10:
                print("Did you know the number 10 is the base of the decimal system?\n")
            else:
                print("But quite a low number.\n")
        else:
            print("And guess what, it's an odd number.\n")
        break
    except ValueError:
        print("Value error: invalid entry, enter a valid number.")

# Reading preference
question1 = input("Do you like reading? (yes/no): ").lower()
if question1 == "yes":
    print("\nThere are some books available, hope you like them.\n")
    time.sleep(2)

    # Book class
    class Book:
        def __init__(self, title, author, year_published):
            self.title = title
            self.author = author
            self.year_published = year_published

        def description(self):
            return f"{self.title} by {self.author}, published in {self.year_published}"

    # Predefined books
    books = [
        Book("LITERATURE", "Geoffrey", 1952),
        Book("KFC", "Otafire", 1995),
        Book("CAFE JAVAS", "Charles Dickens", 1997),
        Book("GARDEN CITY", "Abort", 1960),
        Book("A+", "JaneRose", 1913),
        Book("MICROSOFT", "Darlington", 1949),
        Book("TAREHE SITA", "WakaScott", 1925),
        Book("GAME", "Savage", 1851),
        Book("DOWN TOWN", "Jkimz", 1951),
        Book("STATE HOUSE", "1111", 1937),
    ]

    # Display books
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.description()}")

    print("\nPlease wait")
    print("Generating a list of available books sorted by year...")
    time.sleep(3)

    # Sort books by year
    def sort_books_by_year(books):
        return sorted(books, key=lambda book: book.year_published)

    sorted_books = sort_books_by_year(books)

    # Display sorted books
    print("\nLIST OF SORTED BOOKS")
    for book in sorted_books:
        print(f"{book.title} by {book.author}, published in {book.year_published}")

    # Search book by title
    def search_book_by_title(books, title):
        for book in books:
            if book.title.lower() == title.lower():
                print("\nBook found:")
                print(book.description())
                return
        print("\nBook not found.")

    while True:
        title_to_search = input("\nSearch book by title (or type 'exit' to end): ")
        if title_to_search.lower() == "exit":
            print("Exiting the program.")
            break
        search_book_by_title(books, title_to_search)

elif question1 == "no":
    print("Exiting the program.")
