def nodal_prob(base_attack,crit_prob,turns,memo,health):
	"""
	Thinking of the probability of destruction at specific healths of the enemy
	as "nodes", this function computes the destruction probability for k turns.  It takes
	the base attack of the attacker, a dictionarry of the critcal values whose values
	are their probability.  It takes the turns you wish to compute for, an empty dictionarry
	memo for memorization and the health of the defender which would be the node 
	for which you specifically wish to compute probability for
	"""

	turnsless = turns - 1
	nodal_prob = 0 

	for crit in crit_prob:
		total_d = crit + base_attack
		d_diff = health - total_d

		if d_diff not in memo:
			
			if total_d == 0:
				memo[d_diff] = 0
			elif d_diff <= 0:
				memo[d_diff] = 1
			elif turnsless > 0:
				memo[d_diff] = nodal_prob(base_attack,crit_prob,turnsless,memo,d_diff)
		
		if d_diff in memo:
			nodal_prob += memo[d_diff]*crit_prob[crit]
		else:
			nodal_prob += 0

	return nodal_prob

def destroy_prob(attacker, defender, current_tile, turns):

	base_attack = attacker.get_damage(defender,current_tile)
	hp = defender.health
	crit_prob = {-1:0.2, 0:0.5, 1:0.2, 2:0.1}
	prob = [0]

	for i in range(turns+1):
		memo = {}

		prob_i = nodal_prob(base_attack,crit_prob,i,memo,hp)
		prob.append(prob_i)

	return prob
