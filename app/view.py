
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class MainWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            use_pagination=True,
            check=True,
            # name column, width column, sorting function column(optional), custom tooltip
            column_data=[
                #("Nombre",dp(15))
                ("Nombre", dp(30)),
                ("Pedido", dp(15)),
                ("Monto", dp(15)),
                ("Estado", dp(15)),

            ],

            row_data=[
                (
                    "Agos",
                    "AABB23",
                    "2500",
                    "Pagado"
                ),
                (
                    "Juann",
                    "ACBB45",
                    "2500",
                    "Pagado"
                ),
                (
                    "Fede",
                    "DDB425",
                    "2500",
                    "Pagado"
                ),
            ]
        )
        dynamic_content = self.ids.dynamic_content
        dynamic_content.add_widget(self.data_tables)

    def switch_screen(self, screen_name):
        print('cambiando')

        self.ids.scr_mngr.current = screen_name  # Cambiar a la pantalla especificada por el nombre
        print(screen_name)
