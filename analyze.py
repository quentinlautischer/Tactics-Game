def destroy_prob(attacker, defender, current_tile, turns):

	crit_prob = {-1:.2 , 0:.5, 1:.2, 2:.1}
	prob = []    
	d = attacker.get_damage(defender,current_tile)
	hp = defender.health

	for k in range(turns + 1):
		temp = 0
		for i in crit_prob:
			if (i + d) >= hp:
				temp += crit_prob[i]

		hp -= d
		prob.append(temp)



	return prob
