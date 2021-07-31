import pygame, random
from classes.background import Background
from classes.bird import Bird
from classes.pipe import Pipe
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.Font('freesansbold.ttf', 72)
pygame.display.set_caption("Codeology")

def display_score(score):
    score_img = FONT.render("{}".format(score), True, (255, 255, 255))
    SCREEN.blit(score_img, (SCREEN_WIDTH // 2, 60))

def main():
    FPS = 60

    run = True

    # Define a Pygame clock
    clock = pygame.time.Clock()

    # Initialize the background
    bg = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Initialize birds
    Bird.birds = [Bird(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "yellow")]
    
    # Start score at 0
    score = 0

    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in Bird.birds:
                        bird.jump()

        if len(Pipe.pipes) == 0 or Pipe.pipes[-1].right() < SCREEN_WIDTH - 300: 
            bottom_y = random.randint(300, SCREEN_HEIGHT - 200)
            top_y = random.randint(100, bottom_y - 200)
            pipe = Pipe(SCREEN_WIDTH, bottom_y, top_y)

        # Updating and drawing
        dt = 1 / 60
        
        SCREEN.fill((255, 255, 255)) # Clear background
        
        bg.update(dt)
        bg.draw(SCREEN)

        for pipe in Pipe.pipes:
            pipe.update(dt)
            pipe.draw(SCREEN)
            
        for bird in Bird.birds:
            bird.update(dt)

            # Collisions
            for pipe in Pipe.pipes:
                if pipe.collide(bird):
                    Bird.birds.remove(bird)
            if bird.rect.top < 0 or bird.rect.bottom > SCREEN_HEIGHT:
                Bird.birds.remove(bird) 

            bird.draw(SCREEN)

        if len(Bird.birds) == 0:
            break
        
        for pipe in Pipe.pipes:
            if pipe.right() < SCREEN_WIDTH // 2 and not pipe.scored:
                pipe.scored = 1
                score += 1

        display_score(score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()