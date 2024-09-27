
import pygame as pg
import time

pg.init()
FPS = 240
WIDTH, HEIGHT = 1600, 900+100
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('Py Paint     '+ str(round(clock.get_fps(), 1)))
mouse_pos = pg.mouse.get_pos()
mouse_click = True
shapes = []
color = (255, 0, 0)

def update():
    text = 'NAME IT'
    running = True
    while running:
        pg.draw.rect(screen, (50, 50, 50), pg.Rect(120, 20, 100, 50))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                return False
            
            
        pg.display.update(pg.Rect(120, 20, 100, 50))
            
        
    name = ''
    surface = pg.Surface(1600, 900)
    for i in shapes:
        if i[0] == 'circle': pg.draw.circle(surface, i[1], i[2], i[3])
        if i[0] == 'rect': pg.draw.rect(surface, i[1], pg.Rect(i[2][0], i[2][1], i[3], i[3]))
    pg.image.save(surface, name+'.png')

class UI():
    def __init__(self):
        self.R = 255
        self.G = 0
        self.B = 0
        self.scale = 20
        self.shape = 'circle'
        self.font32 = pg.font.Font('freesansbold.ttf', 32)
        self.font48 = pg.font.Font('freesansbold.ttf', 48)
        self.buttons_pan = [(self.font48.render('File', True, (255, 255, 255)), self.font48.render('File', True, (255, 255, 255)).get_rect(center=(50, 50))),
                            (self.font48.render('Scale', True, (255, 255, 255)), self.font48.render('Scale', True, (255, 255, 255)).get_rect(center=(200, 50))),
                            (self.font48.render('Shapes', True, (255, 255, 255)), self.font48.render('Shapes', True, (255, 255, 255)).get_rect(center=(400, 50))),
                            (self.font48.render('Color', True, (255, 255, 255)), self.font48.render('Color', True, (255, 255, 255)).get_rect(center=(600, 50))),
                            (self.font48.render('Image', True, (255, 255, 255)), self.font48.render('Image', True, (255, 255, 255)).get_rect(center=(800, 50)))
                            ]
        
        
    def file_button(self):
        save_text = self.font32.render('Save', True, (200, 200, 200))
        save_rect= save_text.get_rect(center=(50, 120))
        pg.draw.rect(screen, (50, 50, 50), save_rect, 0, 5)
        screen.blit(save_text, save_rect)
        load_text = self.font32.render('Load', True, (200, 200, 200))
        load_rect= load_text.get_rect(center=(50, 160))
        pg.draw.rect(screen, (50, 50, 50), load_rect, 0, 5)
        screen.blit(load_text, load_rect)
        pg.display.update()
        running = True
        while running:
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                if pg.mouse.get_pressed()[0]:
                    if save_rect.collidepoint(mouse_pos):
                        return update()
                    else:
                        return True
                    
    def scale_button(self):
        rect = pg.Rect(120-5, 150-5, 100+10, 20+10)
        t_scale = self.font32.render('SCALE : ', True, (200, 200, 200))
        t_scale_rect = t_scale.get_rect(center=(170, 120))
        pg.draw.rect(screen, (50, 50, 50), t_scale_rect, 0, 5)
        screen.blit(t_scale, t_scale_rect)
        pg.draw.rect(screen, (50, 50, 50), rect, 0, 5)
        pg.draw.circle(screen, (255, 255, 255), (self.scale+120, 160), 5)
        pg.display.update(rect)
        running = True
        while running:
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                if pg.mouse.get_pressed()[0]:
                    if rect.collidepoint(mouse_pos):
                        pg.draw.rect(screen, (50, 50, 50), rect, 0, 5)
                        pg.draw.circle(screen, (255, 255, 255), (mouse_pos[0], 160), 5+self.scale/100*5)
                        pg.display.update(rect)
                        self.scale = mouse_pos[0]-120
                    else:
                        time.sleep(0.1)
                        if pg.mouse.get_pressed()[0]:
                            if self.scale<1: self.scale = 1
                            return True
    
    def shape_button(self):
        rect_text = self.font32.render('Rectangle', True, (200, 200, 200))
        rect_rect= rect_text.get_rect(center=(400, 120))
        pg.draw.rect(screen, (50, 50, 50), rect_rect, 0, 5)
        screen.blit(rect_text, rect_rect)
        ci_text = self.font32.render('Circle', True, (200, 200, 200))
        ci_rect= ci_text.get_rect(center=(400, 170))
        pg.draw.rect(screen, (50, 50, 50), ci_rect, 0, 5)
        screen.blit(ci_text, ci_rect)
        pg.display.update([rect_rect, ci_rect])
        running = True
        while running:
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                if pg.mouse.get_pressed()[0]:
                    if rect_rect.collidepoint(mouse_pos):
                        self.shape = 'rect'
                        return True
                    if ci_rect.collidepoint(mouse_pos):
                        self.shape = 'circle'
                        return True
                    else:
                        time.sleep(0.1)
                        if pg.mouse.get_pressed()[0]:    
                            return True
                    
    def color_button(self):
        rect0 = pg.Rect(550-5, 150-5, 100+10, 20+10)
        rect1 = pg.Rect(550-5, 230-5, 100+10, 20+10)
        rect2 = pg.Rect(550-5, 310-5, 100+10, 20+10)
        r_scale = self.font32.render('RED : ', True, (255, 0, 0))
        g_scale = self.font32.render('GREEN : ', True, (0, 255, 0))
        b_scale = self.font32.render('BLUE : ', True, (0, 0, 255))
        r_scale_rect = r_scale.get_rect(center=(600, 120))
        g_scale_rect = g_scale.get_rect(center=(600, 200))
        b_scale_rect = b_scale.get_rect(center=(600, 280))
        pg.draw.rect(screen, (50, 50, 50), r_scale_rect, 0, 5)
        pg.draw.rect(screen, (50, 50, 50), g_scale_rect, 0, 5)
        pg.draw.rect(screen, (50, 50, 50), b_scale_rect, 0, 5)
        screen.blit(r_scale, r_scale_rect)
        screen.blit(g_scale, g_scale_rect)
        screen.blit(b_scale, b_scale_rect)
        pg.draw.rect(screen, (50, 50, 50), rect0, 0, 5)
        pg.draw.rect(screen, (50, 50, 50), rect1, 0, 5)
        pg.draw.rect(screen, (50, 50, 50), rect2, 0, 5)
        pg.draw.circle(screen, (255, 255, 255), (self.R/255*100+550, 160), 5)
        pg.draw.circle(screen, (255, 255, 255), (self.G/255*100+550, 240), 5)
        pg.draw.circle(screen, (255, 255, 255), (self.B/255*100+550, 320), 5)
        pg.display.update([rect0, rect1, rect2, r_scale_rect, g_scale_rect, b_scale_rect])
        running = True
        while running:
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                if pg.mouse.get_pressed()[0]:
                    if rect0.collidepoint(mouse_pos):
                        pg.draw.rect(screen, (50, 50, 50), rect0, 0, 5)
                        pg.draw.circle(screen, (255, 255, 255), (mouse_pos[0], 160), 5)
                        pg.display.update(rect0)
                        self.R = mouse_pos[0]-550
                    elif rect1.collidepoint(mouse_pos):
                        pg.draw.rect(screen, (50, 50, 50), rect1, 0, 5)
                        pg.draw.circle(screen, (255, 255, 255), (mouse_pos[0], 240), 5)
                        pg.display.update(rect1)
                        self.G = mouse_pos[0]-550
                    elif rect2.collidepoint(mouse_pos):
                        pg.draw.rect(screen, (50, 50, 50), rect2, 0, 5)
                        pg.draw.circle(screen, (255, 255, 255), (mouse_pos[0], 320), 5)
                        pg.display.update(rect2)
                        self.B = mouse_pos[0]-550
                    else:
                        time.sleep(0.1)
                        if pg.mouse.get_pressed()[0]:
                            if self.R<1: self.R = 1
                            if self.G<1: self.G = 1
                            if self.B<1: self.B = 1
                            return True
    def image_button(self):
        save_text = self.font32.render('Save', True, (200, 200, 200))
        save_rect= save_text.get_rect(center=(50, 120))
        pg.draw.rect(screen, (50, 50, 50), save_rect, 0, 5)
        screen.blit(save_text, save_rect)
        load_text = self.font32.render('Load', True, (200, 200, 200))
        load_rect= load_text.get_rect(center=(50, 160))
        pg.draw.rect(screen, (50, 50, 50), load_rect, 0, 5)
        screen.blit(load_text, load_rect)
        pg.display.update()
        running = True
        while running:
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if save_rect.collidepoint(mouse_pos):
                        pass
                    else:
                        return True
    def draw(self):
        pg.draw.rect(screen, (50, 50, 50), pg.Rect(0, 0, WIDTH, 100))
        for j in range(len(self.buttons_pan)):
            pg.draw.rect(screen, (255, 255, 255), self.buttons_pan[j][1], 1, 5)
            screen.blit(self.buttons_pan[j][0], self.buttons_pan[j][1])
            if self.buttons_pan[j][1].collidepoint(mouse_pos) and mouse_click:
                if j == 0:
                    return self.file_button()
                if j == 1:
                    return self.scale_button()
                if j == 2:
                    return self.shape_button()
                if j == 3:
                    return self.color_button()
                if j == 3:
                    return self.image_button()
        pg.draw.rect(screen, (self.R, self.G, self.B), pg.Rect(675, 45, 30, 30))
        
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(675, 45, 30, 30), 2)
        return True
    

class Paint():
    def __init__(self):
        self.x, self.y = 0, 0
    def update(self):
        self.x, self.y = mouse_pos
        if mouse_click and mouse_pos[1]>ui.scale+100:
            shapes.append([ui.shape, (ui.R, ui.G, ui.B), (self.x, self.y), ui.scale])
        
        

ui = UI()
paint = Paint()

running = True
while running:
    pg.display.set_caption('Py Paint     '+ str(round(clock.get_fps(), 1)))
    mouse_pos = pg.mouse.get_pos()
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.display.quit()
            pg.quit()
        if pg.mouse.get_pressed()[0]:
            mouse_click = True
        else: mouse_click = False
        
    paint.update()
    running = ui.draw()
    for i in shapes:
        if i[0] == 'circle': pg.draw.circle(screen, i[1], i[2], i[3])
        if i[0] == 'rect': pg.draw.rect(screen, i[1], pg.Rect(i[2][0]-i[3]/2, i[2][1]-i[3]/2, i[3], i[3]))
    pg.display.flip()
    clock.tick(FPS)
    
