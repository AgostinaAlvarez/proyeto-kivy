
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from db.database import connect_to_db,fetch_data_from_table

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('hola')
        self.conection = connect_to_db()
        data = fetch_data_from_table(self.conection)

        print(data)

        # como hacer una peticion a una base de datos mas compleja mediante un boton o algo similar
        #deberia agregar una interza que contenga diferentes tipos de layouts
        # a lo que me refiero es que los diferentes layouts tengan diferentes posiciones dentro del app
        #para
        self.data_tables = MDDataTable(
            size_hint=(0.9, 1),
            use_pagination=True,
            check=True,
            # name column, width column, sorting function column(optional), custom tooltip
            column_data=[
                #("Nombre",dp(15))
                ("Pedido", dp(80)),
                ("Monto", dp(15)),
                ("Estado", dp(40)),
                ("Cliente", dp(15)),

            ],

            row_data=data


        )
        dynamic_content = self.ids.dynamic_content
        dynamic_content.add_widget(self.data_tables)

    def switch_screen(self, screen_name):
        self.ids.scr_mngr.current = screen_name  # Cambiar a la pantalla especificada por el nombre
