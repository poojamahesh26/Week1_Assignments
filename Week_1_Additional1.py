#Write a function check_rating(book) that takes a book dictionary and returns True if the rating is greater than 4.5, and False otherwise. Additionally, modify the function to return 'low' if the rating is less than or equal to 4.0, 'medium' if it's greater than 4.0 but less than or equal to 4.5, and 'high' if it's greater than 4.5.

books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]

def check_rating(book):
    return book["rating"] > 4.5

def check_rating_1(book):
    if book["rating"] <= 4.0:
        return "low"
    elif 4.0 < book["rating"] <= 4.5:
        return "medium"
    else:
        return "high"

for book in books:
    print(f"{book['title']}: {check_rating(book)}")

for book in books:
    print(f"{book['title']}: {check_rating_1(book)}")