# Sort samples into tiers by review count
def sortSamplesIntoTiers(samples, cutoffs):
	tiers = [[], [], [], []]
	for sample in samples:
		tiers[getTier(sample.reviewCount, cutoffs)].append(sample)

	return tiers

# Get 20,000 random businesses (without duplicates)
# SAMPLE_SIZE = 20000
# randomBusinesses  = random.sample(businesses, SAMPLE_SIZE)
# samples = [simplifiedBusiness(randomBusiness) for randomBusiness in randomBusinesses]
# Display all
# for sample in samples:
# 	sample.display()

# reviewCounts = [sample.reviewCount for sample in samples]
# stars = [sample.stars for sample in samples]

# print("{}, {}, {}, {}".format(numpy.percentile(reviewCounts, 25), numpy.percentile(reviewCounts, 50), numpy.percentile(reviewCounts, 75), numpy.percentile(reviewCounts, 100)))