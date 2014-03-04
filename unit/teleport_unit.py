from unit.base_unit import BaseUnit
import unit, helper, effects
from tiles import Tile
import pygame

class TeleportUnit(BaseUnit):
    """
    The basic ground-moving unit.
    
    - Only collides with other ground units
    - Gains bonuses (and debuffs) from tiles.
    """
    def __init__(self, **keywords):
        #load the base class
        super().__init__(**keywords)

        #set unit specific things.
        self.type = "Teleport Unit"
        self.hit_sound = "Wormhole"
        self.hit_effect = effects.Wormhole
        
    def is_stoppable(self, tile, pos):
        """
        Returns whether or not a unit can stop on a certain tile.
        """
        dist = helper.manhattan_dist((self.tile_x, self.tile_y), pos)
        
        # Check if this is too close to stop in
        if (dist < self.min_move_distance):
            return False
            
        return super().is_stoppable(tile, pos)

    # def update(self):
    #     """
    #     Overrides the update function of the Sprite class.
    #     Handles movement.
    #     """
    #     if self._moving:
    #         #checks if path is empty
    #         if not self._path:
    #             #notify not moving
    #             self._moving = False
    #             return
                
    #         #There's a path to move on
    #         else:
                                  
    #             #angle properly
    #             #self.face_vector((dx, dy))

    #             #set the new value
    #             self.tile_x += self._path[-2][1]
    #             self.tile_y += self._path[-2][0]