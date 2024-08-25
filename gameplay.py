import pygame as pg
import visual

pg.init()
running = True
while running:
    pg.display.flip()
    pg.time.Clock().tick(15)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and visual.state == 0 and 82 < pg.mouse.get_pos()[0] < 514 and 82 < \
                pg.mouse.get_pos()[1] < 655:
            visual.mouse_checks()

        if event.type == pg.QUIT:
            running = False

    if visual.state == 1:
        visual.movement()
        opt_fight_loop = 1
        for rps in range(len(visual.rps_instances.copy()) - 1):
            for rps_2 in range(opt_fight_loop, len(visual.rps_instances.copy())):
                if visual.rps_instances[rps].material != visual.rps_instances[rps_2].material:

                    if visual.rps_instances[rps].coords[0] > visual.rps_instances[rps_2].coords[0] >= (
                            visual.rps_instances[rps].coords[0] - 32) \
                            and visual.rps_instances[rps].coords[1] > visual.rps_instances[rps_2].coords[1] >= (
                            visual.rps_instances[rps].coords[1] - 32):
                        visual.fight(visual.rps_instances[rps], visual.rps_instances[rps_2])

                    elif visual.rps_instances[rps].coords[0] < visual.rps_instances[rps_2].coords[0] <= (
                            visual.rps_instances[rps].coords[0] + 32) \
                            and visual.rps_instances[rps].coords[1] < visual.rps_instances[rps_2].coords[1] <= (
                            visual.rps_instances[rps].coords[1] + 32):
                        visual.fight(visual.rps_instances[rps], visual.rps_instances[rps_2])

                    elif visual.rps_instances[rps].coords[0] > visual.rps_instances[rps_2].coords[0] >= (
                            visual.rps_instances[rps].coords[0] - 32) \
                            and visual.rps_instances[rps].coords[1] < visual.rps_instances[rps_2].coords[1] <= (
                            visual.rps_instances[rps].coords[1] + 32):
                        visual.fight(visual.rps_instances[rps], visual.rps_instances[rps_2])

                    elif visual.rps_instances[rps].coords[0] < visual.rps_instances[rps_2].coords[0] <= (
                            visual.rps_instances[rps].coords[0] + 32) \
                            and visual.rps_instances[rps].coords[1] > visual.rps_instances[rps_2].coords[1] >= (
                            visual.rps_instances[rps].coords[1] - 32):
                        visual.fight(visual.rps_instances[rps], visual.rps_instances[rps_2])

            opt_fight_loop += 1

pg.quit()

