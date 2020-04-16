from utils import *
from covid import *

# Problem Set 5: Problem 3
print("loading df_confirmed...")
df_confirmed = loadAndCleanData("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

# Problem Set 5: Problem 5
print("correcting df_confirmed...")
df_confirmed = correctDateFormat(df_confirmed, "Confirmed")

# Problem Set 5: Problem 7
print("loading and correcting df_deaths...")
df_deaths = loadAndCleanData("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
df_deaths = correctDateFormat(df_deaths, "Deaths")

print("loading and correcting df_recovered...")
df_recovered = loadAndCleanData("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
df_recovered = correctDateFormat(df_recovered, "Recovered")

# Problem Set 5: Problem 9
print("merging dataframes...")
df = mergeData(df_confirmed, df_deaths, list(df_confirmed.columns)[:-1])
df = mergeData(df, df_recovered, list(df_confirmed.columns)[:-1])

# Problem Set 5: Problem 11
print("plotting df_confirmed...")
plotTimeline(df, "Date", "Confirmed")
print("plotting df_deaths...")
plotTimeline(df, "Date", "Deaths")
print("plotting df_recovered...")
plotTimeline(df, "Date", "Recovered")

# Problem Set 5: Problem 13
print("plotting all dataframes...")
plotMultipleTimelines([df,df,df], "Date", ["Confirmed", "Deaths", "Recovered"])

# Problem Set 5: Problem 16
print("calculating top correlated for df_confirmed...")
print(topCorrelations(df, "Confirmed", 5))
cList = ['Germany', 'Spain', 'Czechia', 'Morocco', 'Romania', 'Belgium', 'Portugal']
for i in range(len(cList)):
		cList[i] = df[df["Country/Region"] == cList[i]].reset_index()

print("calculating top correlated for df_deaths...")
print(topCorrelations(df, "Deaths", 5))
dList = ['Turkey', 'US', 'Belgium', 'Brazil']
for i in range(len(dList)):
		dList[i] = df[df["Country/Region"] == dList[i]].reset_index()

print("calculating top correlated for df_recovered...")
print(topCorrelations(df, "Recovered", 5))
tList = ['Belgium', 'Spain', 'Poland', 'Turkey', 'Iceland', 'Malaysia', 'Germany','Chile']
for i in range(len(tList)):
		tList[i] = df[df["Country/Region"] == tList[i]].reset_index()

# Problem Set 5: Problem 17
print("plotting top correlated for df_confirmed...")
plotMultipleTimelines(cList, "Date", ["Confirmed","Confirmed","Confirmed","Confirmed","Confirmed","Confirmed","Confirmed"])

print("plotting top correlated for df_deaths...")
plotMultipleTimelines(dList, "Date", ["Deaths","Deaths","Deaths","Deaths"])

print("plotting top correlated for df_recovered...")
plotMultipleTimelines(tList, "Date", ["Recovered","Recovered","Recovered","Recovered","Recovered","Recovered","Recovered","Recovered"])