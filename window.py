import arcade
#Neo-Dev-games
class Ventana (arcade.Window):
    def __init__(self, ancho, alto, titulo):
        super().__init__(ancho, alto, titulo, resizable=False)
        Screenwidth, Screenheight = arcade.window_commands.get_display_size()
        self.set_location(Screenwidth//2-ancho//2,Screenheight//2-alto//2)
        arcade.set_background_color(arcade.color.GREEN)
    def on_draw(self):
        arcade.start_render()

    def on_close(self):
        arcade.close_window()
        arcade.exit()


Ventana(800,600,'Neo-Dev-Games')
arcade.run()