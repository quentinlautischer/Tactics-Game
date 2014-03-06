from unit.teleport_unit import TeleportUnit 
import unit, helper, effects
from tiles import Tile 
import pygame

class Water_warper(TeleportUnit):

	"""
	Akimbo to the warper unit, the Nova class water warper "Angler" is
	an advanced underwater submarine with the ability to immediately destroy
	adjacent targets using Negative-Space-Implosion.  It also features a 
	ranged plasma cannon that can attack a riadius of land.

	Armour: Low
	Speed: High
	Range: Moderate-Low
	Damage: Moderate-Very High
	Special: Cannon blasts affect four adjacent sqaures to target
	Overall Bad Arseness: Top Score

	"""

	sprite = pygame.image.load("assets/novaangler.png")

	def __init__(self, **keywords):
		#load the image for the base class.
		self._base_image = Water_warper.sprite

		#load the base class 
		super().__init__(**keywords)
		self.hit_sound = "Wormhole"

		#set unit specific things.
		self.type = "Water_warper"
		self.speed = 10
		self.max_atk_range = 15
		self.damage = 10
		self.defense = 8
		self.bonus_damage = 2
		self.min_move_distance = 13
		self.hit_effect = effects.wormhole

	def is_passable(self, tile, pos):
		""" 
		Returns whether or no this unit can move over a certian tile.
		"""
		#Return default
		if not super(). is passable(tile,pos):
			return False



		#water units cannot move on ground
		if(tile.type != 'water'):
			return False

		return True