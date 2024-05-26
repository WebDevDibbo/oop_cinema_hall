class Star_Cinema:
    hall_list = []

    def entry_hall(self,new_hall):
        self.hall_list.append(new_hall)



class Hall(Star_Cinema):
   
    def __init__(self,rows,cols,hall_no) -> None:

        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
       
       self.show_list.append((id,movie_name,time))
       self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    
    def book_seats(self,movie_id,seat_no):

        if movie_id in self.seats:
            row , col = seat_no
            if row >= 0 and row <= self.rows and col >= 0 and col <= self.cols:
                if self.seats[movie_id][row][col] == 0:
                    self.seats[movie_id][row][col] = 1
                    print(f'seat ({row}, {col}) booked for show {movie_id}')
                else:
                    print('This seat is already booked')
            else:
                print('invalid seat')
        else:
            print('show id is invalid')


    def view_show_list(self):
        for movie_info in self.show_list:
            id,movie_name,movie_time = movie_info
            print(f'MOVIE NAME:{movie_name}({id}) SHOW ID:{id} TIME:{movie_time}')


    def view_available_seats(self,show_id):
        if show_id in self.seats:
            for row in range(self.rows):
                print(f'[',end="")
                for col in range(self.cols):
                        if col == self.cols-1:
                             print(f'{self.seats[show_id][row][col]}',end="")
                        else:
                            print(f'{self.seats[show_id][row][col]},',end="")
                print(f']')
        else:   
            print('your show_id is invalid')



almas_hall = Hall(7,7,1)


almas_hall.entry_show(111,'PATHAAN','26/05/24 5:00 PM')
almas_hall.entry_show(222,'SALAAR','28/05/24 12:00 PM')



while True:

    print(f'\n1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. Exit\n')
    option = int(input('ENTER OPTION: '))


    if option == 1:
        print('----------------------')
        almas_hall.view_show_list()
        print('----------------------')

    
    elif option == 2:
        id = int(input('ENTER SHOW ID: '))
        print('----------------------')
        almas_hall.view_available_seats(id)
        print('----------------------')


    elif option == 3:
        show_id = int(input('ENTER SHOW ID: '))
        seat_row = int(input('ENTER SEAT ROW: '))
        seat_col = int(input('ENTER SEAT COL: '))
        print('----------------------')
        almas_hall.book_seats(show_id,(seat_row,seat_col))
        print('----------------------')


    
    else:
        break




