import matplotlib.pyplot as plt
import numpy as np

def scatterplot(x, y, xLabel, yLabel, title=None):
	plt.scatter(x,y)
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	if title:
		plt.title(title)
	plt.show()

def boxplot(y, label, title=None):
	plt.boxplot(y)
	plt.ylabel(label)
	if title:
		plt.title(title)
	plt.show()

# plots a histogram of a tier or bucket of data
def plotHistogram(tier, mu, sigma):
	# the mean of the dataset
	mu = round(mu, 2)
	# the standard deviation of the dataset
	sigma = round(sigma, 2)
	#  create a list of ratings (stars) from the dataset
	tierData = [sample.stars for sample in tier]
	# subject to change, shows difference between values
	num_bins = 15

	# create the figure
	fig, ax = plt.subplots()
	# the histogram of the data
	n, bins, patches = ax.hist(tierData, num_bins, density=1)

	# add a line of best fit
	y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
	# plot the line of best fit
	ax.plot(bins, y, '--')
	# set axis labels
	ax.set_xlabel('Ratings out of 5 (stars)')
	ax.set_ylabel('Probability density')
	# create the string to title the plot 
	plotTitle = 'Histogram of Ratings mu=' + str(mu) + ' sigma=' + str(sigma)
	ax.set_title(plotTitle)

	# Tweak spacing to prevent clipping of ylabel
	fig.tight_layout()
	plt.show()	
