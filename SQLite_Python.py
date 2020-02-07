import csv
import os.path
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn=None
    if os.path.isfile(db_file):
        os.remove(db_file)
        conn = sqlite3.connect(db_file)
    else:
        conn = sqlite3.connect(db_file)
    return conn


def create_table(conn, create_table_qr):
    try:
        c = conn.cursor()
        c.execute(create_table_qr)
    except Error as e:
        print(e)


def main():
    database = "mydatabase.db"

    sql_create_projects_table = "CREATE TABLE Project (Name text PRIMARY KEY,Description text NULL,Deadline text NULL)"

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Task (
                                    ID integer PRIMARY KEY,
                                    Priority integer NULL,
                                    Details text NULL,
                                    Status text NULL,
                                    Deadline text NULL,
                                    Completed text NULL,
                                    Project text NOT NULL,
                                    FOREIGN KEY (Project) REFERENCES project (Name)
                                );"""

    # create a database connection
    conn = create_connection(database)
    c=conn.cursor()
    # create tables
    if conn is not None:
        # create project table
        create_table(conn, sql_create_projects_table)
        # get developer detail

        #insert data into project table
        with open('Project.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                c.execute("INSERT INTO Project(Name,Description) VALUES (?,?)",(row[0],row[1]))
        conn.commit()
        sqlite_select_query = """SELECT * from Project"""
        c.execute(sqlite_select_query)
        records = c.fetchall()
        print(records)
        # create task table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
