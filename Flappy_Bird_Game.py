"""
This is the popular game Flappy Bird, trained with Reinforcement Learning.

- Wiliam Lindskog
- First project using Reinforcement Learning
"""
import pickle

import pygame
import neat
import os
from Bird import Bird
from Pipe import Pipe
from Ground import Ground

pygame.font.init()

Window_Width = 500
Window_Height = 800
Generation = 0

Background_Image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
Stat_Fond = pygame.font.SysFont("comicsans", 50)


def draw_window(win, birds, pipes, ground, score, generation):
    """
    Draws windows for main loop
    :param win: window surface
    :param birds: The Bird
    :param pipes: List of pipes
    :param ground: The ground
    :param score: Current score indicator
    :param generation: Current generation indicator
    :return: None
    """
    win.blit(Background_Image, (0, 0))
    for pipe in pipes:
        pipe.draw(win)

    text = Stat_Fond.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(text, (Window_Width - 10 - text.get_width(), 10))

    text = Stat_Fond.render("Generation: " + str(generation), True, (255, 255, 255))
    win.blit(text, (10, 10))

    ground.draw(win)

    for bird in birds:
        bird.draw(win)

    pygame.display.update()


def eval_genomes(genomes, config):
    """
    simulates for current population,
    sets fitness based on their performance in game
    """
    global Generation
    Generation += 1
    nets = []
    ge = []
    birds = []

    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        genome.fitness = 0
        ge.append(genome)

    ground = Ground(730)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((Window_Width, Window_Height))
    clock = pygame.time.Clock()

    score = 0

    is_running = True
    while is_running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
                quit()
                break

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].Pipe_Top.get_width():
                pipe_ind = 1
        else:
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            output = nets[x].activate(
                (bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:
                bird.jump()

        add_pipe = False
        rem = []
        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.crash(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.Pipe_Top.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))

        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        if score > 50:
            break

        ground.move()
        draw_window(win, birds, pipes, ground, score, Generation)

        # break if score gets too big
        if score > 30:
            pickle.dump(nets[0], open("best.pickle", "wb"))
            break


def run(configure_pathway):
    """
    runs NEAT algorithm to train neural network for Flappy Bird
    :param configure_pathway: location
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, configure_pathway)

    # Create population
    p = neat.Population(config)

    # stdout reporter to show progress in the terminal
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run up until 50 generations
    winner = p.run(eval_genomes, 50)

    # Show final stats
    print('n\Best genome: \n{!s}'.format(winner))


# Determine path to configuration file.
if __name__ == "__main__":

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
