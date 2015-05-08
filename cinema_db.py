class CinemaDatabaseManager:

    def __init__(self, conn):
        self.__conn = conn
    GET_ALL_MOVIES_QUERY = """
    SELECT movie_id, movie_name, rating
    FROM Movies ORDER BY rating
    """

    GET_MOVIE_BY_ID_AND_DATE = """
    SELECT a.name, b.data, b.time, b.type
    FROM projections as b JOIN movies as a
    ON a.id = b.movie_id
    WHERE b.movie_id = ? AND b.data = ?
    """

    GET_MOVIE_BY_ID = """
    SELECT a.name, b.data, b.time, b.type
    FROM projections as b JOIN movies as a
    ON a.id = b.movie_id
    WHERE b.movie_id = ?
    """

    #greshno! :D
    GET_TABLE_OF_FREE_SEATS_BY_MOVIE_ID = """
    SELECT a.id, a.data, a.time, a.type,COUNT(a.projection_id) FROM projections as a
    JOIN movies as b ON a.movie_id=b.id
    JOIN reservations as c ON c.projection_id=a.
    WHERE a.projection_id = ?
    """
    GET_NUMBER_OF_FREE_SEATS_BY_PROJECTION_ID = """
    SELECT COUNT(projection_id) FROM reservations
    WHERE projection_id = ?
    """

    def get_all_movies(self):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_ALL_MOVIES_QUERY)
        return result.fetchall()

    def get_all_movies_by_id_and_date(self, movie_id, movie_date):
        cursor = self.__conn.cursor()
        result = cursor.execute(
            self.__class__.GET_MOVIE_BY_ID_AND_DATE, (movie_id, movie_date))
        return result.fetchall()

    def get_all_movies_by_id(self, movie_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_MOVIE_BY_ID, (movie_id, ))
        return result.fetchall()

# printira tabloca po movie id i svpobnodite mesta
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
        pass
