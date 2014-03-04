from unit.teleport_unit import TeleportUnit
import unit, helper, effects
from tiles import Tile
import pygame

class Warper(TeleportUnit):
    """
    Highly advanced soldier with the ability to teleport
    Carries a spear that destroys anything it touches.
    
    Armour: Low
    Speed: High
    Range: Low
    Damage: VERY HIGH
   
    
    Other notes:
    - In order to maintain its high speed, the fighter has fairly low fuel.
      Make well-planned strafing runs and be sure you can get back to a carrier
      in time!
    - When firing at another air unit, this unit does extra damage.
    """
    sprite = pygame.image.load("assets/novavangard.png")
    
    def __init__(self, **keywords):
        #load the image for the base class.
        self._base_image = Warper.sprite

        #load the base class
        super().__init__(**keywords)
        

        #set unit specific things.
        self.type = "Warper"
        self.speed = 10
        self.max_atk_range = 1
        self.damage = 2
        self.defense = 3
        self.bonus_damage = 2
        self.min_move_distance = 8

    def is_passable(self, tile, pos):
        """
        Returns whether or not this unit can move over a certain tile.
        """
        # Return default
        if not super().is_passable(tile, pos):
            return False
    
        #ground units can't travel over water or through walls
        if (tile.type == 'water'):
            return False

        return True

    
    
unit.unit_types["Warper"] = Warper