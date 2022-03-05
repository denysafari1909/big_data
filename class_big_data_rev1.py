import mysql.connector as mysql
# import psycopg2 as psy
import os

class CreateDb:
    def _init_(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def create_db(self, db_name):
        """
        buat database
        """
        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("CREATE DATABASE {}".format(db_name))
        except Error as e:
            print("Error while connecting to MySQL", e)

    def create_table(self, db_name,tb_name,cl_name1, cl_name2):
        """
        menambahkan tabel pada database
        """

        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute(f"USE {db_name}")
                cursor.execute(f"CREATE TABLE {tb_name} ({cl_name1} VARCHAR(255), {cl_name2} VARCHAR(255))")

        except mysql.Error as e:
            print('Tidak bisa konek ke DB', e)

    def insert_value(self, db_name,tb_name,cl_name1, cl_name2,value_input):

        """
        menambahkan value pada tabel
        """
        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute(f"USE {db_name}")
                sql = f"INSERT INTO {tb_name} ({cl_name1}, {cl_name2}) VALUES (%s, %s)"
                val = value_input
                cursor.execute(sql, val)
                conn.commit()

        except mysql.Error as e:
            print('Tidak bisa konek ke DB', e)

        # preparing a cursor object
        # creating database

newdb = CreateDb()
newdb.host = "localhost"
newdb.port = "3306"
newdb.user = "root"
newdb.password=""

newdb.create_db("test_db")
newdb.create_table("test_db","customers","name","address")
newdb.insert_value("test_db","customers","name","address",("dadang","cibitung"))
