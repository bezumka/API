import pymysql
from db.config import db_list


class pySql:
    def __init__(self):
        env = 'DEV'
        db = (pymysql.connect(host=db_list[env]['host'],
                              user=db_list[env]['user'],
                              password=db_list[env]['passwd'],
                              database=db_list[env]['database']))
        self.cursor = db.cursor()

    def smart_query(self, query):
        self.cursor.execute(query)
        results = [field[1:] for field in self.cursor.fetchall()]
        return results
