import pygame as pg
import random


class Sprites:
    def __init__(self, material, spawn_mouse):
        if spawn_mouse[0]:
            self.coords = [pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]
        else:
            self.coords = [spawn_mouse[1], spawn_mouse[2]]
        self.material = material

    def render(self):
        surface.blit(pg.transform.scale(pg.image.load(f'pics/{self.material}.png'), (32, 32)),
                     [self.coords[0], self.coords[1]])

    def update(self):
        chance = random.randint(1, 4)
        if (self.coords[0] + 5) > 514:
            self.coords[0] -= 5
        elif 82 > (self.coords[0] - 5):
            self.coords[0] += 5

        if (self.coords[1] + 5) > 655:
            self.coords[1] -= 5
        elif 82 > (self.coords[1] - 5):
            self.coords[1] += 5

        else:
            if chance == 1:
                self.coords[0] += 5
            elif chance == 2:
                self.coords[0] -= 5
            elif chance == 3:
                self.coords[1] += 5
            else:
                self.coords[1] -= 5


surface = pg.display.set_mode((564, 705))
pg.display.set_caption('Rock Paper Scissors')
pg.display.set_icon(pg.image.load("pics/icon.jpg"))
surface.fill("gray")
pg.draw.line(surface, (59, 59, 59), (50, 50), (50, 655))
pg.draw.line(surface, (59, 59, 59), (50, 50), (514, 50))
pg.draw.line(surface, (59, 59, 59), (50, 655), (514, 655))
pg.draw.line(surface, (59, 59, 59), (514, 50), (514, 655))
rps_instances = []
state_iterator = 0
state = 0
rocks_count = 0
papers_count = 0
scissors_count = 0


def mouse_checks():
    global rocks_count
    global papers_count
    global scissors_count
    global state_iterator
    if pg.mouse.get_pressed()[0]:
        if state_iterator == 0:
            rock = Sprites("rock", (True, 0, 0))
            rock.render()
            rps_instances.append(rock)
            rock.rps_index = rps_instances.index(rock)
            rocks_count += 1

        elif state_iterator == 1:
            paper = Sprites("paper", (True, 0, 0))
            paper.render()
            rps_instances.append(paper)
            paper.rps_index = rps_instances.index(paper)
            papers_count += 1
        else:
            scissors = Sprites("scissors", (True, 0, 0))
            scissors.render()
            rps_instances.append(scissors)
            scissors.rps_index = rps_instances.index(scissors)
            scissors_count += 1
    if pg.mouse.get_pressed()[2]:
        if state_iterator != 2:
            state_iterator += 1
        else:
            state_iterator = 0

    if pg.mouse.get_pressed()[1] and len(rps_instances) != 0 and len(rps_instances) != 1 and not same_material_check():
        global state
        state = 1
        for sprite in rps_instances:
            sprite.render()


def screen_update():
    surface.blit(pg.image.load("pics/bg_in_game.jpg"), (0, 0))
    pg.draw.line(surface, (59, 59, 59), (0, 50), (564, 50), 5)
    pg.draw.rect(surface, "gray", (0, 0, 564, 50))
    pg.font.init()
    my_font = pg.font.SysFont('Mojangles', 20)
    rocks_text = my_font.render(f'Rocks: {rocks_count}', True, (0, 0, 0))
    papers_text = my_font.render(f'Papers: {papers_count}', True, (0, 0, 0))
    scissors_text = my_font.render(f'Scissors: {scissors_count}', True, (0, 0, 0))
    surface.blit(rocks_text, (20, 20))
    surface.blit(papers_text, (232, 20))
    surface.blit(scissors_text, (464, 20))


def movement():
    screen_update()
    for sprite in rps_instances:
        sprite.update()
        sprite.render()


def same_material_check():
    return True if all(
        [True if rps_instances[index].material == rps_instances[index + 1].material else False for index in
         range(len(rps_instances) - 1)]) else False


def fight(first, second):
    global rocks_count
    global papers_count
    global scissors_count
    global state
    if (first.material == "rock" and second.material == "scissors") or (
            first.material == "scissors" and second.material == "rock"):
        if first.material == "rock":
            rps_instances.remove(second)
            rock = Sprites("rock", (False, second.coords[0], second.coords[1]))
            rps_instances.append(rock)
        else:
            rps_instances.remove(first)
            rock = Sprites("rock", (False, first.coords[0], first.coords[1]))
            rps_instances.append(rock)

        rocks_count += 1
        scissors_count -= 1
    elif (first.material == "paper" and second.material == "rock") or (
            first.material == "rock" and second.material == "paper"):
        if first.material == "paper":
            rps_instances.remove(second)
            paper = Sprites("paper", (False, second.coords[0], second.coords[1]))
            rps_instances.append(paper)
        else:
            rps_instances.remove(first)
            paper = Sprites("paper", (False, first.coords[0], first.coords[1]))
            rps_instances.append(paper)

        papers_count += 1
        rocks_count -= 1
    elif (first.material == "scissors" and second.material == "paper") or (
            first.material == "paper" and second.material == "scissors"):
        if first.material == "scissors":
            rps_instances.remove(second)
            scissors = Sprites("scissors", (False, second.coords[0], second.coords[1]))
            rps_instances.append(scissors)
        else:
            rps_instances.remove(first)
            scissors = Sprites("scissors", (False, first.coords[0], first.coords[1]))
            rps_instances.append(scissors)

        scissors_count += 1
        papers_count -= 1
    screen_update()
    for rps in rps_instances:
        rps.render()
    if same_material_check():
        state = 2
        pg.draw.rect(surface, "gray", (0, 0, 564, 50))
        pg.font.init()
        my_font = pg.font.SysFont('Mojangles', 20)
        winner_text = my_font.render(f'WINNER: {rps_instances[0].material}', True, (0, 0, 0))
        surface.blit(winner_text, (225, 20))

