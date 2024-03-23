#Task 1 D: Rewrite the entire Task 1 C using Data frames instead of lists.
import pandas as pd

bookD = ({'book_id': [int(input("Enter a book ID: "))],
                  'title': [input("Enter a book title: ")], 
                  'author': ["MS Mthethwa"], 
                  'status':["Not Available"]
                  })


dfB = pd.DataFrame(bookD)

print("Data Frame for books: ", dfB)


memberD = ({'member_id': [9264], 
                    'name': ["Zama"],
                    'borrowed_books': [[]]
                    })

dfM = pd.DataFrame(memberD)

print("Data Frame for members: ", dfM)