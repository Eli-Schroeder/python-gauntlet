class Loops:

    # Several arrows are flying toward you!

    #     ||||  |  | | ||
    #     vvvv  v  v v vv
    #
    #           O

    # (That is a dramatic recreation, not indicative of where the arrows actually are)

    # Move laterally to dodge the arrows. Use
    # scenario.position
    # to see your current position,

    # Use
    # scenario.is_safe(x)
    # to see if the position at index x (zero-indexed) is safe,

    # Use
    # scenario.spaces()
    # to see how many spaces there are,

    # And use
    # scenario.move_to(x)
    # to move to safety!

    def dodge_projectiles(self, scenario):
        return "skip"

    # Uh oh! More arrows!

    #  ||  ||| | |  |||| | ||||
    #  vv  vvv v v  vvvv v vvvv
    #
    #               O

    # (Again, a dramatic re-enactment, does not indicate actual positions)

    # And it's worse! Your ability to teleport has been removed! Now you must move
    # with scenario.move_left() and scenario.move_right()! What a disaster!

    # At least you still have your time distorter to allow you to move as many times
    # as you want before the arrows progress.

    # scenario.move_left() and scenario.move_right() will each return a boolean. It will
    # be True if the move was completed or False if your character could not move due to
    # being next to a wall.

    def dodge_projectiles_but_harder(self, scenario):
        return "skip"

    # You realize that you could easily re-engineer your teleport ability given just
    # the ability to move left or right with infinite speed. Implement this function
    # so that you will be able to once again simply specify the location you want to
    # go to with just an index.

    def move_to(self, scenario, position):
        return "skip"

