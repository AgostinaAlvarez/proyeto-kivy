#conexion a la base de datos
import mysql.connector
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            database="database",
            user="2qby8a3kdmgyr8olie69",
            host="aws.connect.psdb.cloud",
            password="pscale_pw_LzsxfVUJKcKTPQetxa9WgePiUYRCQBwA5ZAWLGk7sAV"
        )

        return connection
    except mysql.connector.Error as err:
        print(f"Error al connectar a la base de datos: {err}")
        return None
