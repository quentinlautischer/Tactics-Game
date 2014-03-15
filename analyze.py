def nodal_prob(base_attack,crit_prob,turns,memo,health):
	"""
	Thinking of the probability of destruction at specific healths of the enemy
	as "nodes", this function computes the destruction probability for k turns.  It takes
	the base attack of the attacker, a dictionarry of the critcal values whose values
	are their probability.  It takes the turns you wish to compute for, an empty dictionarry
	memo for memorization and the health of the defender which would be the node 
	for which you specifically wish to compute probability for
	"""

	turns_left = turns - 1

	print("Turns left:")
	print(turns_left)
	#nodal_prob = 0 #<-- THIS IS THE ISSUE THIS VARIABLE HAS THE SAME NAME AS THE FUNCTION
	nodally_probular = 0

	print("health_left:")
	for crit in crit_prob:
		total_d = crit + base_attack
		health_left = health - total_d
		print(health_left)
		if (base_attack,turns,health) not in memo:
			
			if total_d == 0:
				nodally_probular += 0
			elif health_left <= 0:
				nodally_probular += 1*crit_prob[crit]
			elif turns_left > 0:
				
				nodally_probular += nodal_prob(base_attack,crit_prob,turns_left,memo,health_left) * crit_prob[crit]
		else:
			nodally_probular += memo[(base_attack,turns,health)]

	memo[(base_attack,turns,health)] = nodally_probular
	if nodally_probular > 1: nodally_probular = 1
	return nodally_probular

def destroy_prob(attacker, defender, current_tile, turns):

	base_attack = attacker.get_damage(defender,current_tile)
	hp = defender.health
	crit_prob = {-1:0.2, 0:0.5, 1:0.2, 2:0.1}
	prob = [0]
	memo = {}

	for i in range(turns+1):
		#memo = {}

		prob_i = nodal_prob(base_attack,crit_prob,i,memo,hp)
		prob.append(prob_i)

	return prob
