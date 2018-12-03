import matplotlib.pyplot as plt


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