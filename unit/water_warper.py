from unit.teleport_unit import TeleportUnit 
import unit, helper, effects
from tiles import Tile 
import pygame

class Water_warper(TeleportUnit):

	"""
	Akimbo to the warper unit, the Nova class water warper "Angler" is
	an advanced underwater submarine with the ability to immediately destroy
	adjacent targets using Negative-Space-Implosion.  Have fun ;)

	Armour: Low
	Speed: High
	Range: Low
	Damage: Very High
	Overall Bad Arseness: Top Score

	"""

	sprite = pygame.image.load("assets/novaangler.png")

	def __init__(self, **keywords):
		#load the image for the base class.
		self._base_image = Water_warper.sprite

		#load the base class 
		super().__init__(**keywords)


		#set unit specific things.
		self.type = "Water_warper"
		self.speed = 15
		self.max_atk_range = 1

		self.damage = 50
		self.defense = 3
		self.bonus_damage = 2
		self.min_move_distance = 13


	def is_passable(self, tile, pos):
		""" 
		Returns whether or no this unit can move over a certian tile.
		"""
		#Return default
		if not super().is_passable(tile,pos):
			return False



		#water units cannot move on ground
		if(tile.type != 'water'):
			return False

		return True


	def can_hit(self, target_unit):
		"""
		Determines whether a unit can hit another unit.
        
		Overrides because tanks can't hit planes.
		"""
		# If it's an air unit return false
		if not isinstance(target_unit, unit.water_unit.WaterUnit):
			return False
	        
		# Not an air unit, return true
		return True


unit.unit_types["Water-Warper"] = Water_warper