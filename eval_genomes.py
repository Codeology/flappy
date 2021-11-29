import pygame, random, neat, os
from classes.background import Background
from classes.bird import Bird
from classes.pipe import Pipe
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 768
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.Font('freesansbold.ttf', 72)
pygame.display.set_caption("NEAT - Flappy Bird")

def display_score(score):
    score_img = FONT.render("{}".format(score), True, (255, 255, 255))
    SCREEN.blit(score_img, (SCREEN_WIDTH // 2, 60))

def remove_bird(i, genomes, nets, score):
    genomes[i].fitness += score
    Bird.birds.pop(i)
    genomes.pop(i)
    nets.pop(i)

def eval_genomes(genomes, config):
    FPS = 60
    frame = 0

    run = True

    # Define a Pygame clock
    clock = pygame.time.Clock()

    # Initialize the background
    bg = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Setup genomes
    Bird.birds = []
    Pipe.pipes = []
    ge = []
    nets = []
    for genome_id, genome in genomes:
        Bird.birds.append(Bird(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, Bird.COLORS[genome_id % 6]))
        ge.append(genome)
        nets.append(neat.nn.FeedForwardNetwork.create(genome, config))
        genome.fitness = 0

    # Start score at 0
    score = 0

    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if len(Pipe.pipes) == 0 or Pipe.pipes[-1].right() < SCREEN_WIDTH - 300: 
            bottom_y = random.randint(300, SCREEN_HEIGHT - 200)
            top_y = random.randint(100, bottom_y - 200)
            pipe = Pipe(SCREEN_WIDTH, bottom_y, top_y)

        for i, bird in enumerate(Bird.birds):
            for pipe in Pipe.pipes:
                if pipe.right() >= SCREEN_WIDTH // 2:
                    closest_pipe = pipe
                    break
            output = nets[i].activate((bird.rect.y, abs(closest_pipe.top_pipe_y() - bird.rect.y), (closest_pipe.bottom_pipe_y() - bird.rect.y)))
            if output[0] > 0.5:
                bird.jump()

        # Updating and drawing
        dt = 1 / 60
        
        SCREEN.fill((255, 255, 255)) # Clear background
        
        bg.update(dt)
        bg.draw(SCREEN)

        for pipe in Pipe.pipes:
            pipe.update(dt)
            pipe.draw(SCREEN)
            
        for i, bird in enumerate(Bird.birds):
            bird.update(dt)

            # Collisions
            for pipe in Pipe.pipes:
                if pipe.collide(bird):
                    remove_bird(i, ge, nets, score)
            if bird.rect.top < 0 or bird.rect.bottom > SCREEN_HEIGHT:
                remove_bird(i, ge, nets, score)

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

# Setup the NEAT Neural Network
def run(config_path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(eval_genomes, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)