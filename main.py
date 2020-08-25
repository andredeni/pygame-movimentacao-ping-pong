import pygame

pygame.init()

window = pygame.display.set_mode([800, 580])

circX = 200
circY = 200
speedX = 1
speedY = 1

clock = pygame.time.Clock()
while True:
  window.fill((255, 255, 255))

  pygame.draw.circle(
    window,
    (255, 0, 0),
    [circX, circY],
    70
  )

  circX = circX + speedX  
  circY = circY + speedY

  if circX < 0 or circX > 700:
    speedX = -speedX
  if circY < 0 or circY > 480:
    speedY = -speedY

  pygame.display.update()
  clock.tick(60)