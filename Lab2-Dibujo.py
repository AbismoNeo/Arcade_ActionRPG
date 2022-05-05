import arcade, random
from arcade import csscolor
# Neo-Dev-games
from arcade.color import ATOMIC_TANGERINE


class Ventana (arcade.Window):
    def __init__(self, ancho, alto, titulo):
        super().__init__(ancho, alto, titulo, resizable=False)
        # Obtenemos ancho y alto y acomodamos la pantalla en el centro
        Screenwidth, Screenheight = arcade.window_commands.get_display_size()
        self.set_location(Screenwidth//2-ancho//2, Screenheight//2-alto//2)
        # Ponemos el fondo de color
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()

    def on_close(self):
        arcade.close_window()
        arcade.exit()


def paredes(cx, cy, ancho, alto, corn=False):
    # Pared
    arcade.draw_rectangle_filled(cx, cy, ancho, alto, (255, 127, 80))
    arcade.draw_rectangle_outline(cx, cy, ancho, alto, (210, 105, 30), 1)
    # Corniza
    if corn == True:
        arcade.draw_rectangle_filled(cx, cy+50, ancho+10, 10, (255, 127, 80))
        arcade.draw_rectangle_outline(cx, cy+50, ancho+10, 10, (210, 105, 30), 1)

def puertas(cx,cy,ancho,alto):
    #Izquierda
    arcade.draw_rectangle_filled(cx-(ancho/4), cy, ancho/2, alto, arcade.csscolor.CHOCOLATE)
    arcade.draw_rectangle_outline(cx-(ancho/4), cy, ancho/2, alto, arcade.csscolor.BROWN, 1)
    #Vidrios
    arcade.draw_rectangle_filled(cx-(ancho/4), cy-(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_outline(cx-(ancho/4), cy-(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.VIOLET, 1)
    arcade.draw_rectangle_filled(cx-(ancho/4), cy+(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_outline(cx-(ancho/4), cy+(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.VIOLET, 1)    
    #Derecha
    arcade.draw_rectangle_filled(cx+(ancho/4), cy, ancho/2, alto, arcade.csscolor.CHOCOLATE)
    arcade.draw_rectangle_outline(cx+(ancho/4), cy, ancho/2, alto, arcade.csscolor.BROWN, 1)
    #Vidrios
    arcade.draw_rectangle_filled(cx+(ancho/4), cy-(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_outline(cx+(ancho/4), cy-(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.VIOLET, 1)
    arcade.draw_rectangle_filled(cx+(ancho/4), cy+(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_outline(cx+(ancho/4), cy+(alto/4), (ancho/2)-4, (alto/2)-4, arcade.csscolor.VIOLET, 1)        

def escaleras(cx,cy,ancho):
    #Escalones
    alto=12
    cy = cy -56
    arcade.draw_rectangle_filled(cx, cy,  ancho, alto, arcade.csscolor.LIGHT_GRAY)
    arcade.draw_rectangle_outline(cx, cy, ancho, alto, arcade.csscolor.DARK_GRAY, 1)    
    arcade.draw_rectangle_filled(cx, cy-(alto),  ancho, alto, arcade.csscolor.GRAY)
    arcade.draw_rectangle_outline(cx, cy-(alto), ancho, alto, arcade.csscolor.DARK_GRAY, 1)    
    arcade.draw_rectangle_filled(cx, cy-(alto*2),  ancho, alto, arcade.csscolor.LIGHT_GRAY)
    arcade.draw_rectangle_outline(cx, cy-(alto*2), ancho, alto, arcade.csscolor.DARK_GRAY, 1)    
    arcade.draw_rectangle_filled(cx, cy-(alto*3),  ancho, alto, arcade.csscolor.GRAY)
    arcade.draw_rectangle_outline(cx, cy-(alto*3), ancho, alto, arcade.csscolor.DARK_GRAY, 1)   
    #Camino
    arcade.draw_polygon_filled(((cx-ancho/2,cy-(alto*3)-3),
                               (300,0),
                               (500,0),
                               (cx+ancho/2,cy-(alto*3)-3)
                               ),arcade.csscolor.DIM_GRAY)
    #Muretes
    #Izquierda
    arcade.draw_rectangle_filled(cx-75, cy-20, 50, 50, (255, 127, 80))
    arcade.draw_rectangle_outline(cx-75, cy-20, 50, 50, (210, 105, 30), 1)
    #Derecha
    arcade.draw_rectangle_filled(cx+75, cy-20, 50, 50, (255, 127, 80))
    arcade.draw_rectangle_outline(cx+75, cy-20, 50, 50, (210, 105, 30), 1)    
    
def letrero(cx, cy, ancho, alto):
    # Pared
    arcade.draw_rectangle_filled(cx, cy, ancho, alto, arcade.csscolor.VIOLET)
    arcade.draw_rectangle_outline(cx, cy, ancho, alto, arcade.csscolor.BLUE_VIOLET, 1)
    arcade.draw_rectangle_filled(cx, cy+1, ancho-10, alto-10, (255, 191, 0))
    arcade.draw_rectangle_outline(cx, cy+1, ancho-10, alto-10, (255, 126, 0), 1)
    arcade.draw_text('SPRINFIELD\nELEMENTARY\nSCHOOL', cx - 41, cy + 11, arcade.csscolor.DARK_GRAY, 8, ancho - 15, "center", "arial", True)
    arcade.draw_text('SPRINFIELD\nELEMENTARY\nSCHOOL', cx - 40, cy + 10, arcade.csscolor.BLACK, 8, ancho - 15, "center", "arial", True)

def pilares(cx, cy,alto):
    arcade.draw_rectangle_filled(cx, cy, 10, alto, arcade.csscolor.VIOLET)
    arcade.draw_rectangle_outline(cx, cy, 10, alto, arcade.csscolor.BLUE_VIOLET, 1)


def ventanita(cx, cy):
    # Marco
    arcade.draw_rectangle_filled(cx, cy, 40, 40, arcade.csscolor.VIOLET)
    arcade.draw_rectangle_outline(cx, cy, 40, 40, arcade.csscolor.BLUE_VIOLET, 1)
    #Corniza Ventana
    arcade.draw_rectangle_filled(cx, cy-20, 50, 5, arcade.csscolor.VIOLET)
    arcade.draw_rectangle_outline(cx, cy-20, 50, 5, arcade.csscolor.BLUE_VIOLET, 1)
    # Vidrios Chicos
    arcade.draw_rectangle_filled(cx-15, cy+9, 7, 17, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(cx - 5, cy+9, 7, 17, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(cx +5, cy + 9, 7, 17, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(cx + 15, cy + 9, 7, 17, arcade.csscolor.LIGHT_BLUE)
    # Vidrio Grande
    arcade.draw_rectangle_filled(cx, cy-9, 35, 14, arcade.csscolor.LIGHT_BLUE)

def nubecitas(cx,cy):
    arcade.draw_ellipse_filled(cx, cy, 40, 20, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(cx+30, cy+11, 40, 40, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(cx+80, cy, 70, 70, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(cx+30, cy, 60, 40, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(cx + 30, cy-15, 60, 40, arcade.csscolor.WHITE)
#    arcade.draw_ellipse_filled(cx, cy, rand1, rand2, arcade.csscolor.WHITE)
#    arcade.draw_ellipse_filled(cx, cy, rand1, rand2, arcade.csscolor.WHITE)
#    arcade.draw_ellipse_filled(cx, cy, rand1, rand2, arcade.csscolor.WHITE)
#    arcade.draw_ellipse_filled(cx, cy, rand1, rand2, arcade.csscolor.WHITE)
#    arcade.draw_ellipse_filled(cx, cy, rand1, rand2, arcade.csscolor.WHITE)

def Ventanita_arco(cx,cy):
    arcade.draw_rectangle_filled(cx, cy+5, 80, 35, arcade.csscolor.VIOLET)
    arcade.draw_rectangle_outline(cx, cy+5, 80, 35, arcade.csscolor.BLUE_VIOLET, 1)
    arcade.draw_ellipse_filled(cx, cy+25, 79, 74, arcade.csscolor.VIOLET)
    arcade.draw_arc_outline(cx, cy+25, 79, 74, arcade.csscolor.BLUE_VIOLET, 0, 180, 2)

    arcade.draw_arc_filled(cx, cy + 25, 70, 68, arcade.csscolor.LIGHT_BLUE, 0, 180)

    arcade.draw_line(cx, cy + 25, cx-25, cy+50, arcade.csscolor.VIOLET,5)
    arcade.draw_line(cx, cy + 25, cx+25, cy+50, arcade.csscolor.VIOLET,5)
    arcade.draw_line(cx, cy + 25, cx, cy+60, arcade.csscolor.VIOLET,5)
    arcade.draw_arc_outline(cx, cy+25, 40, 37, arcade.csscolor.VIOLET, 0, 180, 8)
    
    #Ventanitas Chicas
    arcade.draw_rectangle_filled(cx - 30, cy+7, 16, 27, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(cx - 11, cy+7, 16, 27, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(cx + 9, cy+7, 16, 27, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(cx + 28, cy+7, 16, 27, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_outline(cx - 30, cy+7, 16, 27, arcade.csscolor.VIOLET, 2)
    arcade.draw_rectangle_outline(cx - 11, cy + 7, 16, 27, arcade.csscolor.VIOLET, 2)
    arcade.draw_rectangle_outline(cx + 9, cy + 7, 16, 27, arcade.csscolor.VIOLET, 2)
    arcade.draw_rectangle_outline(cx + 28, cy + 7, 16, 27, arcade.csscolor.VIOLET, 2)

def pasillo(cx1,cy1,cx2,cy2):
    arcade.draw_rectangle_filled()


Ventana(800, 600, 'Neo-Dev-Games')
arcade.start_render()

arcade.draw_rectangle_filled(400, 150, 800, 300, arcade.csscolor.LIGHT_GREEN)

#Frente3
paredes(130, 320, 150, 100, True)
paredes(670, 320, 150, 100, True)

#paredes(50, 150, 230, 130)
#paredes(650, 750, 230, 130)

# Frente2
paredes(300, 380, 200, 100, True)
paredes(300, 280, 200, 100, True)
paredes(500, 380, 200, 100, True)
paredes(500, 280, 200, 100, True)

#paredes(150, 100, 200, 100)
#paredes(450, 200, 200, 100)
#paredes(450, 100, 200, 100)

# Lado Izquierdo
pilares(345, 335, 270) # Mas Larga
pilares(335, 330, 260) # Medio
pilares(325, 325, 250) # Mas Corta
# Lado Derecho
pilares(455, 335, 270) # Mas Larga
pilares(465, 330, 260) # Medio
pilares(475, 325, 250) # Mas Corta
#Mas lejanas
pilares(195, 335, 215) # Medio
pilares(605, 335, 215) # Medio


# Frente1
paredes(400, 400, 100, 100, True)
letrero(400, 325, 100, 50)
paredes(400, 250, 100, 100)
puertas(400, 250, 96, 96)
escaleras(400,250,100)

# Lado Izquierdo
ventanita(230, 380)
ventanita(230, 280)
ventanita(290, 380)
ventanita(290, 280)

# Lado Derecho
ventanita(510, 380)
ventanita(510, 280)
ventanita(570, 380)
ventanita(570, 280)

# Ultimo nivel
ventanita(640, 320)
ventanita(710, 320)
ventanita(90, 320)
ventanita(160, 320)

Ventanita_arco(400,370)

#nubecitas(120,500)

arcade.finish_render()
arcade.run()
