# Sort samples into tiers by review count
def sortSamplesIntoTiers(samples, cutoffs):
	tiers = [[], [], [], []]
	for sample in samples:
		tiers[getTier(sample.reviewCount, cutoffs)].append(sample)

	return tiers

