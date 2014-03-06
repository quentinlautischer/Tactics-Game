def destroy_prob(attacker, defender, current_tile, turns):

	crit_prob = {-1:20 , 0:50, 1:20, 2:10}
	prob = []    
	d = attacker.get_damage(defender,current_tile)
	hp = defender.health

	for k in range(len(turns) + 1):
		temp = 0
		for i in crit_prob:
			if (i + d) >= hp:
				temp += crit_prob[i]

		hp -= d
		prob[k] = temp




    return prob[0]
