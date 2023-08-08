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
    # scenario.move(x)
    # to move to safety!

    def dodge_projectiles(self, scenario):
        raise NotImplementedError()

    # Uh oh! More arrows!

    #  ||  ||| | |  |||| | ||||
    #  vv  vvv v v  vvvv v vvvv
    #
    #               O

    # (Again, a dramatic re-enactment, does not indicate actual positions)

    # And it's worse! Your ability to teleport has been removed! Now you must move
    # with scenario.move_left() and scenario.move_right()! What a disaster!

    def dodge_projectiles_but_harder(self, scenario):
        raise NotImplementedError()