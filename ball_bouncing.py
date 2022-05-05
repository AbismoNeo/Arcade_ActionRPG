""" 
    ############################ NEO - DEV - GAMES ############################
    Aplicacion que crea una pelota que rebota al llegar al borde de la pantalla
    desarrollado con ARCADE PYTHON, dibujado a través de codigo
    ###########################################################################"""
# LIBRERIAS #
import arcade, random
from pathlib import Path
import os,sys

# CONSTANTES GLOBALES #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pelota Rebotando"
SCREEN_COLOR = arcade.csscolor.GRAY
BALL_HEIGHT = 50
BALL_WIDTH = 50
BALL_COLOR = arcade.csscolor.RED
try:
    absolutepath = os.path.abspath(__file__)
    fileDirectory = os.path.dirname(absolutepath)
    SONIDO = os.path.join(fileDirectory,'sound\\boing.mp3')
    BALL_SOUND = arcade.sound.load_sound(SONIDO,False)
    print('CARGADO')
except:
    print('NO CARGADO')




class pelota:
    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        
        self.change_x = 0
        self.change_y = 0
    
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        # Tope Derecha
        if self.center_x > SCREEN_WIDTH - BALL_WIDTH/2:
            self.change_x *= -1
            arcade.sound.play_sound(BALL_SOUND,1.0,-1,False)
        # Tope Arriba   
        if self.center_y > SCREEN_HEIGHT - BALL_HEIGHT/2:
            self.change_y *= -1
            arcade.sound.play_sound(BALL_SOUND,1.0,-1,False)
        # Tope Izquierda
        if self.center_x < BALL_WIDTH/2 :
            self.change_x *= -1
            arcade.sound.play_sound(BALL_SOUND,1.0,-1,False)
        # Tope Abajo
        if self.center_y < BALL_HEIGHT/2:
            self.change_y *= -1
            arcade.sound.play_sound(BALL_SOUND,1.0,-1,False)
    
    def draw(self):
        arcade.draw_ellipse_filled(self.center_x,
                                   self.center_y,
                                   BALL_WIDTH,
                                   BALL_HEIGHT,
                                   BALL_COLOR)

class Juego(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height,title)
        
        self.pelota = pelota()
        self.pelota.center_x = 200
        self.pelota.center_y = 300
        self.pelota.change_x = 2
        self.pelota.change_y = 3
        
        self.background_color = SCREEN_COLOR
    
    def on_update(self, delta_time):
        self.pelota.update()
        
    def on_draw(self):
        self.clear()
        self.pelota.draw()
    
def main():
    Juego(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.run()
    

if __name__ == "__main__":
    main()
        
