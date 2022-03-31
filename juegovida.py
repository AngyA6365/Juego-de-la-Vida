import pygame
import numpy as np 
import time
pygame.init()
width, height = 500, 500
#Crear pantalla  
screen = pygame.display.set_mode ((height, width)) 

bg=25, 25, 25
screen.fill(bg)

#Color de fondo
nxC, nyC = 27, 27

dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC, nyC))

#Aut palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

#Aut mov
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

#Control de ejecución
pauseExect = False

while True: 

    newGameState = np.copy(gameState)
    
    screen.fill(bg)
    time.sleep(0.1)

    #Teclado y Ratón
    ev = pygame.event.get()

    for event in ev: 
        if event.type == pygame.KEYDOWN:
           pauseExect = not pauseExect  

        mouseClick = pygame.mouse.get_pressed()
        print(mouseClick)
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

    for y in range (0, nxC):
        for x in range (0, nyC):

            if not pauseExect:

                n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
                        gameState[(x) % nxC, (y-1) % nyC] + \
                        gameState[(x+1) % nxC, (y-1) % nyC] + \
                        gameState[(x-1) % nxC, (y) % nyC] + \
                        gameState[(x+1) % nxC, (y) % nyC] + \
                        gameState[(x-1) % nxC, (y+1) % nyC] + \
                        gameState[(x) % nxC, (y+1) % nyC] + \
                        gameState[(x+1) % nxC, (y+1) % nyC]

                #Regla 1: Una célula muerta con tres vecinas vivas, vuelve a la vida.
                if gameState [x, y] == 0 and n_neigh == 3:
                    newGameState [x, y] = 1

                    #Regla 2: Una celula con menos de dos o más de tres celulas vecinas vivas, muere.
                elif gameState [x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState [x, y] = 0                                  

            poly =[((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]

            if newGameState [x, y] == 0: 
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)
    pygame.display.flip()   
pass
