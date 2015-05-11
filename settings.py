DB_NAME = "cinema.db"
SQL_FILE = "cinema_tables.sql"
SIZE = 10
HELP_INFO = """
*spell show_movies - print all movies
*spell show_movie_projections <movie_id> [<date>] - print all projections of a given movie for the given date (date is optional);
For each projection, show the total number of spots available.
*make_reservation:
- choose a name
- choose number of tickets
- choose a projection
- for each ticket choose a tuple (row, col).
- finalize spell, save all the info
*give_up - gives up the make_reservation
*cancel_reservation <name> - disintegrate given person's reservation
*exit - exit the cinema manager
*help - show a list of learned spell
"""
