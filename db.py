import os
import psycopg2
import re


def get_db_params():
    # local
    db_parameters = {
        'dbname': 'postgres',
        'host': '130.61.49.87',
        'port': '5432',
        'user': 'postgres',
        'password': 'mysecretpassword'
    }

    return db_parameters


class PostgresDB(object):

    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def __get_db_connection__(self):
        return psycopg2.connect(dbname=self.dbname, host=self.host, port=self.port,
                                user=self.user, password=self.password)

    def execute_querry(self, sql):
        conn = self.__get_db_connection__()
        cursor = conn.cursor()

        retval = None
        try:
            cursor.execute(sql)

            # Для SELECT
            if re.fullmatch(r'\s*select.*(.*\s*)*', sql, re.IGNORECASE):
                retval = []
                for row in cursor:
                    retval.append(row)  # список кортежей

            # Для INSERT
            elif re.fullmatch(r'\s*insert.*(.*\s*)*', sql, re.IGNORECASE):
                conn.commit()

            # Для UPDATE
            elif re.fullmatch(r'\s*update.*(.*\s*)*', sql, re.IGNORECASE):
                conn.commit()

            # Для DELETE
            elif re.fullmatch(r'\s*delete.*(.*\s*)*', sql, re.IGNORECASE):
                conn.commit()

            # Для CREATE
            elif re.fullmatch(r'\s*create.*(.*\s*)*', sql, re.IGNORECASE):
                conn.commit()
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()

        return retval
