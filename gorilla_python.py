# ## Gorilla Wars 0.1 ## #

import arcade, math, random
import arcade.gui as gui

SCREEN_ANCHO = 800
SCREEN_ALTO = 600
SCREEN_TITULO = "Gorilla Wars"
SCORE = 0
VIDAS = 3
NIVEL = 1
PLAYER1NAME = ''
PLAYER2NAME = ['LUIS',
               'PEDRO', 
               'MOISES', 
               'OMAR', 
               'MARTIN', 
               'JUAN', 
               'FERNANDO', 
               'DANIEL', 
               'ROGELIO', 
               'MARIO',
               'ROBERTO',
               'MIGUEL',
               'HENRY',
               'MANUEL',
               'LENIN',
               'ANTONIO',
               'DAVID',
               'JORGE',
               'RICARDO',
               'NEO']



class QuitButton(arcade.gui.UIFlatButton):
    def __init__(self):
        self.color = arcade.csscolor.DARK_RED
        self.text = 'QUITAR'    
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class OkButton(arcade.gui.UIFlatButton):
    def __init__(self):
        self.color = arcade.csscolor.DARK_GREEN
        self.text = 'ACEPTAR'
        
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        self.on_click = self.on_click
        
    
class PlayButton(arcade.gui.UIFlatButton):
    def __init__(self):
        self.color = arcade.csscolor.DARK_GOLDENROD
        self.text = 'JUGAR'    
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        Ventana.clear()
        Juego()
        
class HomeButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        Ventana.clear()
        Instrucciones()


class InputText(arcade.gui.UIInputText):
    def __init__(self):
        self.color = arcade.csscolor.LIGHT_GRAY
        self.font_size = 24
        self.width = 200
        self.text ='Introduce Nombre de Jugador'
        
            
        
class Ventana (arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_ANCHO, SCREEN_ALTO, SCREEN_TITULO, resizable=False)
        self.clear
        self.manager = gui.UIManager()
        self.manager.enable()
        self.background_color=arcade.csscolor.AQUAMARINE
        

    def on_draw(self):
        arcade.start_render()

    def on_close(self):
        arcade.close_window()
        arcade.exit()
    
    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.ESCAPE:
            Ventana.__init__()
        elif symbol == arcade.key.ENTER and len(Nombre.text)>0:
            PLAYER1NAME = Nombre.text
        elif len(Nombre.text) > 15 :
            symbol = None 
    
    def Instrucciones(self):
        # This function prints the instructions. #
        INSTRUCCIONES= """
    Bienvenido a Gorilla Wars : 
    La idea es derrotar al otro jugador con una banana explosiva; para esto
    debe ingresar el ángulo y la fuerza del tiro, Suerte!!
    
    Presiona ENTER para empezar a jugar
    
    
    
        
    Desarrollado por:  Neo - Dev - Games
        """
        arcade.draw_text(INSTRUCCIONES,50,(SCREEN_ALTO/3)*2,arcade.csscolor.BLACK, 20, bold = True)
        self.v_box = gui.UIBoxLayout()
        self.v_box.add(PlayButton)
        self.v_box.add(QuitButton)
                     


def calculate_distance(psi, angle_in_degrees):
    """ Calculate the distance the mudball flies. """
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance


def get_user_input(name):
    """ Get the user input for psi and angle. Return as a list of two
    numbers. """
    # Later on in the 'exceptions' chapter, we will learn how to modify
    # this code to not crash the game if the user types in something that
    # isn't a valid number.
    psi = float(input(name + " charge the gun with how many psi? "))
    angle = float(input(name + " move the gun at what angle? "))
    return psi, angle


def get_player_names():
    """ Get a list of names from the players. """
    INSTRUCCION= "ESCRIBE TU NOMBRE DE JUGADOR: "
    arcade.draw_text(INSTRUCCION,50,(SCREEN_ALTO/3)*2,arcade.csscolor.BLACK, 20, bold = True)    
    done = False
    players = []
    # Mientras no sea ENTER sigue escribiendo
    while done == False:
        # Si la tecla 
        if  Ventana.on_key_press()  == arcade.key.ENTER and  len(Nombre.text)==0 :
            INSTRUCCION = "INGRESE EL NOMBRE (Presione << ENTER >> PARA AGREGAR Y SALIR): "
            arcade.draw_text(INSTRUCCION,50,(SCREEN_ALTO/3),arcade.csscolor.BLACK, 20, bold = True)    
            player = Nombre.text
        elif Ventana.on_key_press()  == arcade.key.ENTER and  len(Nombre.text)>0 :
            players.append(player)
            done = True
        
    players.append(PLAYER2NAME[NIVEL-1])
    
    
    return players


def process_player_turn(player_name, distance_apart):
    """ The code runs the turn for each player.
    If it returns False, keep going with the game.
    If it returns True, someone has won, so stop. """
    psi, angle = get_user_input(player_name)

    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart

    # By looking ahead to the chapter on print formatting, these
    # lines could be made to print the numbers is a nice formatted
    # manner.
    if difference > 1:
        print("You went", difference, "yards too far!")
    elif difference < -1:
        print("You were", difference * -1, "yards too short!")
    else:
        print("Hit!", player_name, "wins!")
        return True

    print()
    return False


def main():
    """ Main program. """
    Ventana()
    Nombre = InputText()
    # Get the game started.
    #print_instructions()
    player_names = get_player_names()
    # Creamos la posicion de los jugadores
    # Player 1
    location_player1x = random.randrange(20,380)
    location_player1y = random.randrange(20,400)
    # Player 2
    location_player2x = random.randrange(420,780)
    location_player2y = random.randrange(20,400)
    #Calculamos la distancia entre los dos
    distance_apart = location_player2x - location_player1x

    # Keep looking until someone wins
    done = False
    while not done:
        # Loop for each player
        for player_name in player_names:
            # Process their turn
            done = process_player_turn(player_name, distance_apart)
            # If someone won, 'break' out of this loop and end the game.
            if done:
                break
    # RUN RUN RUN ...
    arcade.run


if __name__ == "__main__":
    main()