# from flask.ext import mysql
from flaskext.mysql import MySQL


from flask import app, Flask

global __mydb


# def server_connection():
#     __mydb = None
#     if __mydb is None:
#         __mydb = mysql.connector.connect(
#             host='localhost:3306',
#             user='root',
#             password='',
#             database='planner'
#         )
#     return __mydb


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'MyDB'
app = Flask(__name__)
mysql = MySQL()
app.config.setdefault('MYSQL_DATABASE_HOST', 'localhost')
app.config.setdefault('MYSQL_DATABASE_PORT', 3306)
app.config.setdefault('MYSQL_DATABASE_USER', 'root')
app.config.setdefault('MYSQL_DATABASE_PASSWORD', '')
app.config.setdefault('MYSQL_DATABASE_PASSWORD', '')
app.config.setdefault('MYSQL_DATABASE_DB', 'planner')
mysql.init_app(app)


def insert_venue( venues):
    conn = mysql.connect()
    cursor=conn.cursor()
    query = (
        "INSERT INTO venue(venuename,venuetype,venueaddress,venuecost,venuecontact,venuelimit,venueimage) VALUES (%s,%s,%s,%s,%s,%s,%s)")
    data = (venues['venuename'], venues['venuetype'], venues['venueaddress'],
            venues['venuecost'], venues['venuecontact'], venues['venuelimit'], venues['venueimage'])
    s=cursor.execute(query, data)
    conn.commit()
    cursor.close()
    return  venues



    # connection.commit()


# if __name__ == '__main__':
    # connection = server_connection()
