import animation

class Wormhole(animation.Animation):
    """
    An animated explosion effect.
    """
    def __init__(self, pos):
        """
        Initialize the sprite effect.
        """
        animation.Animation.__init__(self,
                                     "assets/blackhole.png",
                                     20,
                                     20,
                                     0.2,
                                     animation.Mode.OneShot)
        self.rect.topleft = pos
