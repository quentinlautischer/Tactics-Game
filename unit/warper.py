from unit.teleport_unit import TeleportUnit
import unit, helper, effects
from tiles import Tile
import pygame

class Warper(TeleportUnit):
    """
    The Nova Vangard special attack force unit this is soley one man.  But one man is 
    all you need when you have TELEPORTAION MOTHER FUNNER!  Boasting a Tesla class 
    7.8 Mega Warp-Unit teleportation module he can be in and out before anyone is the wiser.
    I know what your thinking, 7.8 Mega Warp-Units? You dont need nearly that many to simply
    teleport the average man, and you would be correct! The extra 7.7 Mega Warp-Units is so
    he can WARP HIS ENEMIES TO OBLIVION!  Thats right, fitted with the Negative-Space-Implosion
    module expasion simply close a wormhole on anyone you wish to smite, be smited or have smoten!
    
    Armour: Low
    Speed: High
    Range: Low
    Damage: VERY HIGH
    Cool?: Yes
   
    
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
        self.damage = 50
        self.defense = 0
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