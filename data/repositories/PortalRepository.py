from mysql.connector import connection

from models.order import Order


class PortalRepository:

    def __init__(self):
        self.dict = {
            'host': 'localhost',
            'database': 'labs_db',
            'user': 'user',
            'password': 'password'
        }

    def get_all(self):
        try:
            conn = connection.MySQLConnection(**self.dict)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM orders')
            result = cursor.fetchall()

            for oc in result:
                order = Order(oc)
                print(order)

            return result
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()
