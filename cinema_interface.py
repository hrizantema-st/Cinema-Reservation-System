class CliInterface:

    def __init__(self, cinema_manager):
        self.__cinema = cinema_manager

    def __command_dispatcher(self, command):
        command_list = command.split(" ")
        while command_list[0] != "exit":
            if len(command_list) == 1:
                if command_list[0] == "show_movies":
                    self.show_movies()
                elif command_list[0] == "finalize":
                    for seat in for_finalize["list_of_seats"]:
                        reserve_row = seat[0]
                        reserve_column = seat[1]
                        self.__cinema.add_new_reservation(for_finalize["res_name"], for_finalize[
                                                          "projection_id"], reserve_row, reserve_column)
                elif command_list[0] == 'give_up':
                    start_over = input("Do you wan to start over? yes/no: ")
                    if start_over == 'yes':
                        self.make_reservation()
                elif command_list[0] == 'make_reservation':
                    for_finalize = self.make_reservation()
                elif command_list[0] == "help":
                    self.helper()
            elif len(command_list) == 2:
                if command_list[0] == "show_movie_projections":
                    self.get_all_movies_by_id(command_list[1])
                elif command_list[0] == "cancel_reservation":
                    self.__cinema.delete_reservation(command_list[1])
            elif len(command_list) == 3:
                if command_list[0] == "show_movie_projections":
                    self.get_all_movies_by_id_and_date(
                        command_list[1], command_list[2])
            else:
                print("No such command!")

    def start(self):
        while True:
            command = input("Enter command")
            self.__command_dispatcher(command)

    def show_movies(self):
        all_movies = self.__cinema.get_all_movies()
        print("\n".join([movie["name"] for movie in all_movies]))

    def get_all_movies_by_id(self, num):
        by_id = self.__cinema.get_all_movies_by_id(num)
        if len(by_id) > 0:
            print(by_id)
        else:
            print ("Invalid input!")

    def get_all_movies_by_id_and_date(self, num, date):
        by_id_and_date = self.__cinema.get_all_movies_by_id_and_date(num, date)
        if len(by_id_and_date) > 0:
            print(by_id_and_date)
        else:
            print ("Invalid input!")

    def how_many_free_seats(self, projection_id, number_of_tickets):
        number_of_free_seats = self.__cinema.get_num_of_free_seats_by_projection_id(
            projection_id)
        if number_of_free_seats < number_of_tickets:
            return False
        return True

    def matrix_print(self, seats):

    list_of_lists = []
    for row in range(0, 10):
        new_row = []
        for elem in range(0, 10):
            new_row.append(".")
        list_of_lists.append(new_row)

    for seat in seats:
        i = seat['row'] - 1
        j = seat['column'] - 1
        list_of_lists[i][j] = "X"

    for each in list_of_lists:
        print(each)

    return matrix

    def make_reservation(self):
        reservation_name = input("Choose name: ")
        number_of_tickets = input("Choose number of tickets: ")
        self.show_movies()
        while True:
            reservation_movie_id = input("Choose movie id: ")
            self.__cinema.get_num_of_free_seats_by_movie_id(
                reservation_movie_id)
            wanted_projection_id = input("Choose projection id: ")
            if self.how_many_free_seats(reservation_movie_id, number_of_tickets):
                break
            else:
                print("There are no more available seats! Enter new id: ")
        list_of_not_available_seats = self.__cinema.show_all_available_spots_matrix(
            wanted_projection_id)
        matrix = self.matrix_print(list_of_not_available_seats)
        count = 0
        list_of_reserved_seats = []
        while count < number_of_tickets:
            seat_tuple = input("Choose a seat: ")
            if matrix[seat_tuple[0] - 1][seat_tuple[1] - 1] == 'X':
                print("This seat is taken")
            elif seat_tuple[0] > 10 or seat_tuple[0] < 1 or seat_tuple[1] > 10 or seat_tuple[1] < 1:
                print("There is no such seat")
            else:
                count += 1
                list_of_reserved_seats.append(seat_tuple)
        res = {}
        res["res_name"] = reservation_name
        res["list_of_seats"] = list_of_reserved_seats
        res["projection_id"] = wanted_projection_id
        return res

    def helper(self):
        pass
