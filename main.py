import json
import numpy
import calculations

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

SAMPLE_SIZE = 1000
CUTOFFS = [100, 500, 800]

file = open('data.json')
businesses = json.load(file)['businesses']

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