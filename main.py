import json
import numpy
import random
import calculations
import plots

file = open('data.json')
businesses = json.load(file)['businesses']

class simplifiedBusiness:
	# Construct a simplifiedBusiness (obj) from a business (dict)
	def __init__(self, business):
		# if not simplifiedBusiness.validateBusiness(business):
		# 	print('BUSINESS VALIDATION FAILED.')
		self.businessID = business['business_id']
		self.reviewCount = business['review_count']
		self.stars = business['stars']

		if not self.validate():
			print('BUSINESS VALIDATION FAILED')

	# Validate if a simplified business has all the required attributes
	def validate(self):
		return self.businessID and self.reviewCount and self.stars

	def display(self):
		print('({}, {}, {})'.format(self.businessID, self.reviewCount, self.stars))

# Determine the tier a sample belongs to
# based on the number provided
def getTier(number, cutoffs):
	for i in range(len(cutoffs)):
		lowerBound = cutoffs[i-1] if i > 0 else 0
		upperBound = cutoffs[i]
		if lowerBound <= number and number < upperBound:
			return i
	return len(cutoffs)

def part1():
	# Get 20,000 random businesses (without replacement)
	SAMPLE_SIZE = 20000
	randomBusinesses  = random.sample(businesses, SAMPLE_SIZE)
	samples = [simplifiedBusiness(randomBusiness) for randomBusiness in randomBusinesses]
	# Display all
	# for sample in samples:
	# 	sample.display()

	reviewCounts = [sample.reviewCount for sample in samples]
	stars = [sample.stars for sample in samples]

	print("{}, {}, {}, {}".format(numpy.percentile(reviewCounts, 25), numpy.percentile(reviewCounts, 50), numpy.percentile(reviewCounts, 75), numpy.percentile(reviewCounts, 100)))
	plots.scatterplot(stars, reviewCounts, "Ratings", "Review Counts", "Review Counts vs. Ratings")
	plots.boxplot(stars, "Ratings", "Ratings")
	plots.boxplot(reviewCounts, "Review Counts", "Review Counts")

def part2():
	# Get 1,000 random businesses for each bucket (without replacement)
	SAMPLE_SIZE = 1000
	CUTOFFS = [100, 500, 800]

	tiers = [[], [], [], []]
	while min([len(tier) for tier in tiers]) < SAMPLE_SIZE:
		randomBusiness  = calculations.getRandomSample(businesses)
		tierIndex = getTier(randomBusiness["review_count"], CUTOFFS)
		if len(tiers[tierIndex]) < SAMPLE_SIZE:
			sample = simplifiedBusiness(randomBusiness)
			if sample not in tiers[tierIndex]:
				tiers[tierIndex].append(sample)

	for tier in tiers:
		average, margin, lower, upper = calculations.getCI([sample.stars for sample in tier])
		sigma = numpy.std([sample.stars for sample in tier])
		print("{}, {}+-{}=({},{})".format(sigma, average, margin, lower, upper))

part1()