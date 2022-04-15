import pygame

WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Grid')


WHITE = (255, 255,255)
BLACK = (0, 0,0)





def main():

    pygame.init()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.fill(WHITE)
        for i in range(1,30):
            pygame.draw.line(WIN, BLACK, (20,20*i), (580,20*i) , 2)
            pygame.draw.line(WIN, BLACK, (20*i, 20), (20*i, 580), 2)
        pygame.display.update()
            
        




if __name__ == '__main__':
    main()
    pygame.quit()

