# esta va a ser la api con todas sus respectivas peticiones


def fetch_data_from_table(connection):
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT pedidos.id,pedidos.total,pedidos.estado,clientes.nombre FROM pedidos JOIN clientes ON pedidos.idCliente = clientes.id")
            data = cursor.fetchall()
            cursor.close()
            return data
        except mysql.connector.Error as err:
            print(f"Error al consultar a la base de datos: {err}")
            return []
    else:
        return []