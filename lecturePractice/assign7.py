# class Library:
#     def __init__(self, listofBooks):
#         self.books = listofBooks
#         self.issued_books = {}  # To track issued books

#     def displayAvailableBooks(self):
#         print("Available Books:")
#         for book in self.books:
#             print(book)

#     def borrowBook(self, student_name, bookname):
#         if bookname in self.books:
#             self.books.remove(bookname)
#             self.issued_books[bookname] = student_name
#             print(f"{student_name} has borrowed the book '{bookname}'.")
#         else:
#             print("Sorry, this book is not available for borrowing.")

#     def returnBook(self, bookname):
#         if bookname in self.issued_books:
#             student_name = self.issued_books.pop(bookname)
#             self.books.append(bookname)
#             print(f"{bookname} has been returned by {student_name}")
#         else:
#             print("This book was not issued from this library.")

#     def donateBook(self, bookname):
#         self.books.append(bookname)
#         print(f"{bookname} has been donated to the library.")

# class Student:
#    def requestBook(self):
#     bookname = input("Enter the name of the book you want to borrow: ")
#     student_name = input("Enter your name: ")
#     return student_name, bookname



#     def returnBook(self):
#         student_name = input("Enter your name: ")
#         bookname = input("Enter the name of the book you want to return: ")
#         return student_name, bookname

#     def donateBook(self):
#         bookname = input("Enter the name of the book you want to donate: ")
#         return bookname

# # Main Execution
# if __name__ == "__main__":
#     book_list = ["Book1", "Book2", "Book3", "Book4", "Book5"]
#     IIITlibrary = Library(book_list)
#     student = Student()

#     while True:
#         print("\nMenu:")
#         print("1. Display Available Books")
#         print("2. Borrow a Book")
#         print("3. Return a Book")
#         print("4. Donate a Book")
#         print("5. Display Issued Books Tracking")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             IIITlibrary.displayAvailableBooks()
#         elif choice == "2":
#             student_name, book = student.requestBook()  # Get student_name here
#             IIITlibrary.borrowBook(student_name, book) 
#         elif choice == "3":
#             student_name, book = student.returnBook()
#             IIITlibrary.returnBook(book)
#         elif choice == "4":
#             book = student.donateBook()
#             IIITlibrary.donateBook(book)
#         elif choice == "5":
#             print("Issued Books Tracking:")
#             for book, student_name in IIITlibrary.issued_books.items():
#                 print(f"{book} - Borrowed by {student_name}")
#         elif choice == "6":
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")


class Multiplex():
    Number_of_Halls=10
    Address="IIIT KALYANI"
class Hall():
    # def __init__(self):
    # movie_name=["RRR","LUCIFER","THE FAMILY MAN","PANCHAYAT"]
    # ticket_price= [20,30,40,100]
    # ticket_price=20 
 
    def calculate_ticket_price(self, movie_name, number_of_tickets):
        if movie_name=="LUCIFER":
            ticket_price=20
            bought_tickets_price=int(number_of_tickets*20)
            return bought_tickets_price

    def check_seat_availability(self, movie_name, total_tickets):
        tt=total_tickets
        if movie_name=="LUCIFER":
            if tt!=0: 
            # print("NOW",total_tickets-number_of_tickets,"SEATS ARE AVAILABLE")
                return "HURRAH!!!!!!SEATS ARE AVAILABLE"
            # else:
            #     print("SORRY! NO MORE TICKETS LEFT!")
            # else:
            #     print("ALL SEATS ARE AVAILABLE")
            else:
                return "SORRY! YOU CAN BOOK ONLY",tt,"TICKETS!! NO MORE TICKETS LEFT!"
    def get_seat_numbers(self):
         
        # i=0
        # for C[i] in list_available_seat_number:
        #     list_available_seat_number.remove(C[i])
        return list_available_seat_number

    def book_ticket(self, movie_name, number_of_tickets):
        # if movie_name=="LUCIFER":
        #     print("TOTAL BOOKED TICKETS ARE ",number_of_tickets)
        #     print("YOU HAVE SUCCESSFULY BOOKED SEAT")
        # return C 
        booked_seats=[]         
        i=0
        for C[i] in list_available_seat_number:
            booked_seats.append(C[i])
            list_available_seat_number.remove(C[i])
        return booked_seats    
    def cancel_ticket(self, seat_number):
        list_available_seat_number.extend(seat_number)
        return seat_number
m=Hall()
h=Multiplex()

list_available_seat_number=["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"] 
total_tickets=10 

while True:
    b=int(input("give: "))
    if b==0:
        break
    movie_name=input("WHICH MOVIE YOU WANT TO WATCH ?--")
    csa=m.check_seat_availability(movie_name,total_tickets)
    print(csa)
    z=m.get_seat_numbers() 
    print("AVAILABLE SEATS ARE:\n",z)
    C = []
    while True:
        a=input("WHICH SEAT YOU WANT (enter '0' to stop) ::")
        if a == '0':
            break    
        C.append(a)
    print("Total Seat List:", C)
    number_of_tickets=len(C)    
    x=m.book_ticket(movie_name,C)
    print("booked ticket",x)    
    fare=m.calculate_ticket_price(movie_name, number_of_tickets)
    print("FARE FOR BOUGHT TICKETS:",fare,"RUPEES") 
    y=m.get_seat_numbers() 
    print("NOW SEATS ARE AVAILABLE::\n",y)
    print("WHICH SEAT YOU WANT TO CANCEL!!!!!")
    seat_number=[]
    while True:
        c=input("WHICH SEAT YOU WANT TO CANCEL(enter '0' to stop)::")
        if c=='0':
            break
        seat_number.append(c)
    g=m.cancel_ticket(seat_number) 
    print("CANCELLED TICKETS:: ",g)