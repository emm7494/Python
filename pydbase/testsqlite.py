import os
from contextlib import contextmanager
import sqlite3
from sqlite3 import Error


@contextmanager
def manage_db_conn(db_filename):
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_file = os.path.join(basedir, f'{db_filename}.db')
    try:
        con = sqlite3.connect(db_file)
        con.row_factory = sqlite3.Row
        yield con
    except Error as err:
        print(f'SQLite, {type(err).__name__}: {err}.')
    except Exception as err:
        print(f'\nPython, {type(err).__name__}: {err}.')
    else:
        print('\nAll operations were successful!!!')
        print(
            f'\nYour database file: "{db_filename}.db" is loacated at: "{db_file}".')
    finally:
        con.close()
        print('\nConnection closed successfully!!!')


def run_sql(*query, db_filename='app'):
    with manage_db_conn(db_filename) as con:
        with con:
            cur = con.cursor()
            try:
                cur.execute(*query)
            except ValueError as err:
                raise err
            else:
                print(f'\nNo error while executing SQL.')


if __name__ == '__main__':
    # main()
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
    run_sql(sql_create_projects_table)
