#Task 1 B: Rewrite the entire task 1 and task 1B without using parameters and arguments in your functions.

#Initialize two data structures to keep track of books and members both represented as lists.
books = []
members = []

#The system features two functions (You must create these functions): add_book and add_member.

#The add_book function takes three parameters (book_id, title, author, status) and appends a new book dictionary to the books list. 
def add_book ():
    books.append({'book_id': int(input("Enter book ID: ")),
                  'title': input("Enter a book title: "), 
                  'author': "MS Mthethwa", 
                  'status':"Not Available"
                  })


#The add_member function, on the other hand, requires two parameters (member_id, name) and appends a new member dictionay to the members list.
#Each member dictionary includes an empty list for borrowed_books to track the IDs of books each member has borrowed.
    
def add_member():
    members.append({'member_id': 9264, 
                    'name': "Zama",
                    'borrowed_books': [2]
                    })
    
"""Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a 
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. """

#call the functions and 
add_book()
add_member()

#write a print statement for them
print("Books: ", books)
print("\nMembers: ", members)