import sqlite3
from sqlite3 import Error


def main():
    db_file = 'pydbase/pysqlite3.db'

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""
    conn = create_connection(db_file)
    if db_file is not None:
        print('Success! Created database connection.')
    else:
        print('Error! Could not create database connection.')


def create_connection(db_file):
    '''create a database connection to SQLite database'''
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
    return None


if __name__ == '__main__':
    main()
