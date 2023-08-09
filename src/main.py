# TODO: Put your names here (entire team)
#
# REMINDER: Define each class in a file of its own,
# with the file name == class name.

import pygame
import sys
# -----------------------------------------------------------------------------
# TODO: Put your IMPORT statements here, e.g.
#   from Fighter import Fighter
# -----------------------------------------------------------------------------

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 650))  # TODO: Choose your own size
    pygame.display.set_caption("My Project")  # TODO: Choose your own title
    background_color = pygame.Color("black")  # TODO: Choose your own color
    clock = pygame.time.Clock()
    frame_rate = 60  # TODO: Choose your own frame rate

    # -------------------------------------------------------------------------
    # TODO: Define your objects (instances of your classes) below here,
    #     fighter = Fighter(screen, 320, 600)
    # -------------------------------------------------------------------------

    while True:
        clock.tick(frame_rate)

        events = pygame.event.get()
        exit_if_time_to_quit(events)
        pressed_keys = pygame.key.get_pressed()
        # ---------------------------------------------------------------------
        # TODO: Handle events below here:
        #  Use code like the following, but for YOUR Game objects.
        #     if pressed_keys[pygame.K_LEFT]:
        #         fighter.move_left()
        #     if key_was_pressed_on_this_cycle(pygame.K_SPACE, events):
        #         fighter.fire()
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # TODO: Below here, ask your objects to "run one cycle" as needed, e.g.
        #     enemy_fleet.run_one_cycle()
        # ---------------------------------------------------------------------

        screen.fill(background_color)
        # ---------------------------------------------------------------------
        # TODO: Below here, draw your objects, e.g.
        #     fighter.draw()
        # ---------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Two handy "helper" functions, used in the game loop above.
# -----------------------------------------------------------------------------
def exit_if_time_to_quit(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()


def key_was_pressed_on_this_cycle(key, events):
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == key:
            return True
    return False


main()
