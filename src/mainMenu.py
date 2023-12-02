import pygame_menu

import drawLine as drawLine
import midpoint as midpoint
import fillPolygons as fillPolygons
import drawPolygons as drawPolygons 
import rayCastingMap as rayCastingMap 
import main as main

def mainMenu():
    menu = pygame_menu.Menu('Grafica', 1150, 800, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Linhas', drawLine.drawLineCanvas)
    menu.add.button('Circulos', midpoint.drawCircleCanvas)
    menu.add.button('Poligonos', drawPolygons.drawPolygonsCanvas)
    menu.add.button('Fill Poligonos', fillPolygons.drawPolygonsCanvas)
    menu.add.button('Ray Casting', rayCastingMap.run)
    menu.add.button('Settings', settingsMenu)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(main.surface)

def settingsMenu():
    menu = pygame_menu.Menu('Settings', 1150, 800, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Line Thickness: ', input_type=pygame_menu.locals.INPUT_INT, default=main.Cosmetics.lineThickness, onchange=lambda value: main.Cosmetics.__setattr__('lineThickness', value))
    menu.add.text_input('Line Color R: ', input_type=pygame_menu.locals.INPUT_INT, default=main.Cosmetics.lineColorR, onchange=lambda value: main.Cosmetics.__setattr__('lineColorR', value))
    menu.add.text_input('Line Color G: ', input_type=pygame_menu.locals.INPUT_INT, default=main.Cosmetics.lineColorG, onchange=lambda value: main.Cosmetics.__setattr__('lineColorG', value))
    menu.add.text_input('Line Color B: ', input_type=pygame_menu.locals.INPUT_INT, default=main.Cosmetics.lineColorB, onchange=lambda value: main.Cosmetics.__setattr__('lineColorB', value))
    menu.add.text_input('Target FPS: ', input_type=pygame_menu.locals.INPUT_INT, default=main.Cosmetics.targetFPS, onchange=lambda value: main.Cosmetics.__setattr__('targetFPS', value))
    menu.add.toggle_switch('Slow Mode: ', default=False, onchange=lambda value: main.Cosmetics.__setattr__('slowMode', value))
    menu.add.button('Clear', clearCanvas)
    menu.add.button('Back', mainMenu)
    
    menu.mainloop(main.surface)

def clearCanvas():
    main.reconstruir.clear()
    dataTela = None
    settingsMenu()