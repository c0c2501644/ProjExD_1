import os

import sys

import pygame as pg



os.chdir(os.path.dirname(os.path.abspath(__file__)))



def main():

    pg.display.set_caption("はばたけ！こうかとん")

    screen = pg.display.set_mode((800, 600))

    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1

    bg_img2 = pg.transform.flip(bg_img, True, False) #練習8

    kk_img = pg.image.load("fig/3.png")#練習3

    kk_img = pg.transform.flip(kk_img, True, False)

    kk_rct = kk_img.get_rect() #練習10.1

    kk_rct.center = 300,200 #練習10.2

    tmr = 0

    while True:

        for event in pg.event.get():

            if event.type == pg.QUIT: return

        
        key_lst = pg.key.get_pressed()
        dx = -1  
        dy = 0
        
        if key_lst[pg.K_UP]:    
            dy -= 1
        if key_lst[pg.K_DOWN]:  
            dy += 1
        if key_lst[pg.K_LEFT]:  
            dx -= 1
        if key_lst[pg.K_RIGHT]: 
            dx += 2 
        
        kk_rct.move_ip(dx, dy)

        x = tmr % 3200 #練習5

        screen.blit(bg_img, [-x, 0]) #練習2

        screen.blit(bg_img2, [-x+1600, 0])#練習4   

        screen.blit(bg_img, [-x+3200, 0])#練習7

        screen.blit(kk_img, kk_rct)

        pg.display.update()

        tmr += 1        

        clock.tick(200) #練習6





if __name__ == "__main__":

    pg.init()
    main()
    pg.quit()
    sys.exit()