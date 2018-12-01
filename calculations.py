import numpy
import random

# Z value for 95% confidence interval
Z = 1.96

def getRandomSample(population):
	randomIndex = random.randint(0, len(population)-1)
	return population[randomIndex]

def getAverage(dataset):
	return sum(dataset)/len(dataset)

def getMarginOfError(dataset):
	sd = numpy.std(dataset)
	l = len(dataset)
	return Z * sd / l**0.5

def getCI(dataset):
	average = getAverage(dataset)
	margin = getMarginOfError(dataset)
	return average, margin, average-margin, average+margin