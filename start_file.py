import sqlite3
from settings import DB_NAME
from cinema_interface import CliInterface
from cinema_db import CinemaDatabaseManager


def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    cinema_manager = CinemaDatabaseManager(conn)
    interface = CliInterface(cinema_manager)

    interface.start()

if __name__ == "__main__":
    main()
