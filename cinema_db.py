from settings import CINEMA_SIZE

class CinemaDatabaseManager:

    def __init__(self, conn):
        self.__conn = conn

    GET_ALL_MOVIES_QUERY = """
    SELECT "[" || id || "] - " || name || ": (" || rating || ")" as movie_info FROM movies ORDER BY rating DESC
    """

    GET_MOVIE_BY_ID = """
    SELECT "[" || b.id || "]  -  " ||  b.data || " " ||  b.time || " (" ||  b.type || ")"  as proj_for_current_movie
    FROM projections as b JOIN movies as a
    ON a.id = b.movie_id
    WHERE b.movie_id = ? ORDER BY b.data
    """

    GET_MOVIE_BY_ID_AND_DATE = """
    SELECT "[" || b.id || "]  -  " ||   b.time || " (" ||  b.type || ")"  as proj_for_current_movie
    FROM projections as b JOIN movies as a
    ON a.id = b.movie_id
    WHERE b.movie_id = ? AND b.data = ?
    """

    GET_TABLE_OF_FREE_SEATS_BY_MOVIE_ID = """
    SELECT "[" || b.id || "]  -  " || b.data || " " ||   b.time || " (" ||  b.type || ") "  || (100 - count(c.projection_id)) ||" spots available" as proj_for_current_movie
    FROM  projections as b
    LEFT JOIN reservations as c  ON b.id = c.projection_id
    WHERE b.movie_id = ?
    GROUP BY c.projection_id;
    """

    GET_NUMBER_OF_FREE_SEATS_BY_PROJECTION_ID = """
    SELECT (100 - COUNT(projection_id)) as free_seats_for_pr FROM reservations
    WHERE projection_id = ?;
    """

    GET_ALL_FREE_SEATS_BY_PROJECTION_ID = """
    SELECT row, column FROM reservations WHERE projection_id = ?
    """

    ADD_NEW_RESERVATION = """
    INSERT INTO reservations (username, projection_id, row, column) VALUES(?, ?, ?, ?)
    """

    DELETE_RESERVATION_BY_NAME = """
    DELETE FROM reservations WHERE username = ?
    """

    def get_all_movies(self):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_ALL_MOVIES_QUERY)
        return result.fetchall()

    def get_all_movies_by_id(self, movie_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_MOVIE_BY_ID, (movie_id, ))
        return result.fetchall()

    def get_all_movies_by_id_and_date(self, movie_id, movie_date):
        cursor = self.__conn.cursor()
        result = cursor.execute(
            self.__class__.GET_MOVIE_BY_ID_AND_DATE, (movie_id, movie_date))
        return result.fetchall()

    def get_num_of_free_seats_by_movie_id(self, movie_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(
            self.__class__.GET_TABLE_OF_FREE_SEATS_BY_MOVIE_ID, (movie_id, ))
        return result.fetchall()

    def get_num_of_seats_by_projection_id(self, projection_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(
            self.__class__.GET_NUMBER_OF_FREE_SEATS_BY_PROJECTION_ID, (projection_id, ))
        return result.fetchone()

    def show_all_available_spots_matrix(self, projection_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(
            self.__class__.GET_ALL_FREE_SEATS_BY_PROJECTION_ID, (projection_id, ))
        return result.fetchall()

    def add_new_reservation(self, username, projection_id, row, column):
        cursor = self.__conn.cursor()
        cursor.execute(
            self.__class__.ADD_NEW_RESERVATION, (username, projection_id, row, column))

    def delete_reservation(self, username):
        cursor = self.__conn.cursor()
        cursor.execute(
            self.__class__.DELETE_RESERVATION_BY_NAME, (username, ))
