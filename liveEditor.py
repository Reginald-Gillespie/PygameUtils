import pygame
import time
import math

pygame.init()

pygame.display.set_caption('Live Pygame Viewer')
infoObject = pygame.display.Info()
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




# Enter the code to live update here, it will update every time you save
#-#-#-#-#-# Begin Live Code #-#-#-#-#-#

canvas.fill((0, 0, 0))

pygame.draw.polygon(canvas, (200, 200, 200), [  
                    ( 25, 0 ),
                    ( 0, 50 ),
                    ( 50, 50 )  ])

#_#_#_#_#_#  End Live Code  #_#_#_#_#_#






is_running = True
clock = pygame.time.Clock()
while is_running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.dict["unicode"] == "q":
                is_running = False

    with open("liveEditor.py", "r") as code_file:
        code = code_file.read()
        code = code[code.rfind("#-#-#"+"-#-#-#"):code.find("#_#_#"+"_#_#_#")]

    canvas.fill((127, 127, 127))

    try:
        exec(code)
    except Exception as e:
        print("Error:", e)
        time.sleep(0.5)

    pygame.display.flip()
