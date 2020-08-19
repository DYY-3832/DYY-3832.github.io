import pygame,sys,os
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("shutdown")
word = "关机"
font = pygame.font.SysFont("kaiti",100)
text = font.render(word,True,(255,0,0))
rect1 = pygame.Rect(200,100,300,250)
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTENDOWN:
      x = event.pos[0]
      y = event.pos[1]
      if rect1.colliderect(x,y):
        os.system("shutdown -s -t 0")
  screen.fill((255,255,255))
  screen.blit(text,rect1)
  pygame.display.update()
