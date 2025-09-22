# class Multiplex():
#     Number_of_Halls = 10
#     Address = "IIIT KALYANI"

# class Hall():
#     def __init__(self):
#         self.movie_name = ["RRR", "LUCIFER", "THE FAMILY MAN", "PANCHAYAT"]
#         self.ticket_price = {"RRR": 20, "LUCIFER": 30, "THE FAMILY MAN": 40, "PANCHAYAT": 100}
#         self.total_tickets = 10
#         self.seat_numbers = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]

#     def calculate_ticket_price(self, movie_name, number_of_tickets):
#         return self.ticket_price[movie_name] * number_of_tickets

#     def check_seat_availability(self, movie_name):
#         available_seats = 0
#         for seat in self.seat_numbers:
#             if seat.startswith(movie_name[0]):
#                 available_seats += 1
#         if available_seats > 0:
#             return f"HURRAH!!!!!! {available_seats} SEATS ARE AVAILABLE"
#         else:
#             return "SORRY! NO MORE TICKETS LEFT!"

#     def book_ticket(self, movie_name, seat_list):
#         booked_seats = []
#         for seat in seat_list:
#             try:
#                 self.seat_numbers.remove(seat)
#                 booked_seats.append(seat)
#             except ValueError:
#                 print("Invalid seat number or seat already booked")
#         return booked_seats

#     # def cancel_ticket(self, movie_name, seat_list):
#     #     canceled_seats = []
#     #     for seat in seat_list:
#     #         try:
#     #             self.seat_numbers.append(seat)
#     #             canceled_seats.append(seat)
#     #         except ValueError:
#     #             print("Invalid seat number or seat not booked")
#     #     return canceled_seats
#     def cancel_ticket(self, seat_number):
#         i=0
#         for i in seat_number:
#             list_available_seat_number.append(seat_number[i])
#         return seat_number

# m = Hall()
# h = Multiplex()

# while True:
#     b = int(input("give: "))
#     if b == 0:
#         break
#     movie_name = input("WHICH MOVIE YOU WANT TO WATCH ?--")
#     csa = m.check_seat_availability(movie_name)
#     print(csa)
#     z = m.seat_numbers
#     print("AVAILABLE SEATS ARE:\n", z)
#     C = []
#     while True:
#         a = input("WHICH SEAT YOU WANT (enter '0' to stop) ::")
#         if a == '0':
#             break
#         C.append(a)
#     print("Total Seat List:", C)
#     number_of_tickets = len(C)
#     x = m.book_ticket(movie_name, C)
#     print("booked ticket", x)
#     fare = m.calculate_ticket_price(movie_name, number_of_tickets)
#     print("FARE FOR BOUGHT TICKETS:", fare, "RUPEES")
#     y = m.seat_numbers
#     print("NOW SEATS ARE AVAILABLE::\n", y)
#     print("WHICH SEAT YOU WANT TO CANCEL!!!!!")
#     seat_number = []
#     while True:
#         if c == 0:
#             break
#         seat_number.append(c)
#         c = int(input("ENTER CHOICE"))
#     g = m.cancel_ticket(seat_number)
#     print(g)
 