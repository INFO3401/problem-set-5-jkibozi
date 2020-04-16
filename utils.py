import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def loadAndCleanData(file):
	dataset = pd.read_csv(file, encoding='utf-8')
	dataset.fillna(value=0, inplace=True)
	# this next line was taken from https://stackoverflow.com/questions/22649693/drop-rows-with-all-zeros-in-pandas-data-frame
	dataset = dataset.loc[(dataset!=0).any(axis=1)] # this lets me drop rows where all values are 0
	return dataset

# Problem Set 5: Problem 8
def mergeData(dataset1, dataset2, columnList):
	dataset = dataset1.merge(dataset2, on=columnList)
	return dataset

# Problem Set 5: Problem 10
def plotTimeline(dataset, time_col, val_col):
	sns.lineplot(data=dataset, x=time_col, y=val_col)
	plt.show()

# Problem Set 5: Problem 12
def plotMultipleTimelines(dataset, time_col, val_col):
	colors=['red','orange','yellow','green','blue','purple','pink','brown']
	for i in range(len(val_col)):
		sns.lineplot(data=dataset[i], x=time_col, y=val_col[i], color=colors[i])
	plt.show()