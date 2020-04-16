import pandas as pd

# Problem Set 5: Problem 4 / Problem 6
def correctDateFormat(dataset,columnName):
	dataset = dataset.melt(id_vars=dataset.columns[0:4], var_name="Date", value_name=columnName)
	dataset["Date"] = pd.to_datetime(dataset["Date"])
	return dataset

# Problem Set 5: Problem 14
def aggregateCountry(dataset, target, country):
	temp_data = dataset.pivot_table(values=target, index='Date', columns='Country/Region', aggfunc='first')
	return pd.DataFrame(temp_data[country])

# Problem Set 5: Problem 15
def topCorrelations(dataset, target, number):
	dataset2 = dataset.pivot_table(values=target, index='Date', columns='Country/Region', aggfunc='first')
	for country in dataset2.columns:
		if dataset2[country][-1] < 500:
			dataset2.drop(country,axis='columns',inplace=True)
	dataset2 = dataset2.corr()
	countries  = dataset2.columns
	repeatList = []
	repeatList2 = []

	for country1 in countries:
		for country2 in countries:
			if country1 != country2:
				if [country1,country2] not in repeatList and [country2,country1] not in repeatList:
					repeatList.append([country1,country2])
					repeatList2.append(dataset2[country1][country2])

	dataset3 = pd.DataFrame(list(zip(repeatList,repeatList2)), columns=['Pairs','Corr'])
	dataset3.sort_values(by='Corr',inplace=True, ascending=False)
	return(dataset3.iloc[:number])