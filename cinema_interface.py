class CliInterface:

    def __init__(self, cinema_manager):
        self.__cinema = cinema_manager

    def __command_dispatcher(self, command):
        command_list = command.split(" ")
        while command_list[0] != "exit":
            if len(command_list) == 1:
                if command_list[0] == "show_movies":
                    self.show_movies()
            elif len(command_list) == 2:
                if command_list[0] == "show_movie_projections":
                    self.get_all_movies_by_id(command_list[1])
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
        # print(matrix)
