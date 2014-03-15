def nodal_prob(base_attack,crit_prob,turns,memo,health):
	"""
	Thinking of the probability of destruction at specific healths of the enemy
	as "nodes", this function computes the destruction probability for k turns.  It takes
	the base attack of the attacker, a dictionarry of the critcal values whose values
	are their probability.  It takes the turns you wish to compute for, an empty dictionarry
	memo for memorization and the health of the defender which would be the node 
	for which you specifically wish to compute probability for
	"""

	turns_left = turns - 1 #If 0 we dont want to call recursivley again

	nodally_probular = 0 #Set the base probability for this node to be 0

	for crit in crit_prob: #Look through the critical probabilitiess
		total_damage = crit + base_attack
		health_left = health - total_damage
		if (base_attack,turns,health) not in memo:
			"""
			This if statement is to make sure we didnt already memmoize the 
			probability for this specific instance
			"""
			
			if total_damage == 0: #Did we do no damage? Then with that crit there is 0 prob
				nodally_probular += 0
			elif health_left <= 0: #Did we kill him? probility is one times the prob of this crit
				nodally_probular += 1*crit_prob[crit]
			elif turns_left > 0: #call recursion if we want to look any turns deeper
				
				nodally_probular += nodal_prob(base_attack,crit_prob,turns_left,memo,health_left) * crit_prob[crit]
		else:
			nodally_probular += memo[(base_attack,turns,health)] #We had it memoized already

	memo[(base_attack,turns,health)] = nodally_probular #memoize the result
	if nodally_probular > 1: nodally_probular = 1 #If prob is bigger than one, we still killed it
	return nodally_probular

def destroy_prob(attacker, defender, current_tile, turns):
	"""
	destroy_prob returns the an array of len(turns + 1).  Each k in the array is the 
	probability of destroying the defender in k turns taking into account defenses, tile 
	defense bonus, attack power and critical attack probabilities
	"""


	base_attack = attacker.get_damage(defender,current_tile)
	hp = defender.health
	crit_prob = {-1:0.2, 0:0.5, 1:0.2, 2:0.1}
	prob = [0]
	memo = {}

	for i in range(turns+1):

		prob_i = nodal_prob(base_attack,crit_prob,i,memo,hp)
		prob.append(prob_i)

	return prob
