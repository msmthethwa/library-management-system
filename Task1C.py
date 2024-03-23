#Task 1 C: Rewrite the entire task 1B without using functions

#Initialize two data structures to keep track of books and members both represented as lists.
books = []
members = []

bookD = ({'book_id': int(input("Enter book ID: ")),
                  'title': input("Enter a book title: "), 
                  'author': "MS Mthethwa", 
                  'status':"Not Available"
                  })

books.append(bookD)


memberD = ({'member_id': 9264, 
                    'name': "Zama",
                    'borrowed_books': []
                    })

members.append(memberD)

#write a print statement for them
print("Books: ", books)
print("\nMembers: ", members)