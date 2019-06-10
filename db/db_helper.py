import pymysql
from db.config import db_list, codes


class pySql:
    def __init__(self):
        self.codes = codes
        env = 'DEV'
        self.db = (pymysql.connect(host=db_list[env]['host'],
                                   user=db_list[env]['user'],
                                   password=db_list[env]['passwd'],
                                   database=db_list[env]['database']))
        self.cursor = self.db.cursor()

    def smart_query(self, query):
        self.cursor.execute(query)
        results = [field[1:] for field in self.cursor.fetchall()]
        return results

    def smart_query_full(self, query):
        self.cursor.execute(query)
        result = [field for field in self.cursor.fetchall()]
        self.cursor.close()

        return result

    def get_column_names(self, query):
        self.cursor.execute(query)
        column_names = [column[0] for column in self.cursor.description]

        return column_names

    def insert_data_to_db(self, table, columns, values):
        try:
            self.cursor.execute(
                'INSERT INTO {0} ({1}) VALUES (\'{2}\')'.format(table, ", ".join(columns), "', '".join(values)))
            self.db.commit()

            return self.codes["code_1"]
        except pymysql.IntegrityError:

            return self.codes["code_2"]

    def call_procedure(self, procedure, value):
        self.cursor.callproc(procedure, value)
        results = self.cursor.fetchone()

        return results[0]
