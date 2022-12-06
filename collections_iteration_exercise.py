'''
Task: Write a program which initialises a dictionary mapping 
book titles to authors, and searches the dictionary for books
by an author provided as input by the user.
'''

books = {
         "the lord of the rings":"j.r.r. tolkien",
         "the hobbit":"j.r.r. tolkien", 
         "james and the giant peach":"roald dahl",
         "the handmaid's tale":"margaret atwood", 
         "matilda":"roald dahl", 
         "the blind assassin":"margaret atwood", 
         "the silmarillion":"j.r.r. tolkien"
        }

def search_for_books(user_author, books):
    if not user_author.lower() in map(str.lower, books.values()): # extra functionality
        print("No books found")
    else: # core solution
        for book, author in books.items():
            if author.lower() == user_author.lower():
                print(book)

while True:
    user_author = input("Please enter an author: ")
    if not user_author:
        break
    search_for_books(user_author, books)
