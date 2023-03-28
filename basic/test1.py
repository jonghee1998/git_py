import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("핀볼 게임")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("스페이스바 눌림")
    
    # 게임 창 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()

# now add one more print
print(1+1)
 
print("hi")


