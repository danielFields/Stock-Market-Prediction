#Plot target variable
#Set x axis ticks
tickers = np.arange(17)*1000
dates = data1["Date"].iloc[tickers].values

#Relabel x_axis ticks with Date
for i in np.arange(len(dates)):
    dates[i] = dates[i][:7]
    

plt.figure(figsize = (15,9))
plt.plot(data1["CLOSE"], label = "Close")
plt.xticks(ticks = tickers,labels = dates, rotation = 315)
plt.ylabel("Close Price")
plt.title("Histroric SP500 Close Price")

#Visualize changes in distribution of target variable over different decades.

#Split Target Variable by decade
#1950 - 1960
fifty_2_sixty = data1.iloc[np.arange(2013)]["CLOSE"]

#1960 - 1970
sixty_2_seventy = data1.iloc[np.arange(2013,4502)]["CLOSE"]

#1970 - 1980
seventy_2_eighty = data1.iloc[np.arange(4502,7028)]["CLOSE"]

#1980 - 1990
eighty_2_ninety = data1.iloc[np.arange(7028,9809)]["CLOSE"]

#1990 - 2000
ninety_2_00 = data1.iloc[np.arange(9809,12084)]["CLOSE"]

#2000 - 2010
OO_2_2010 = data1.iloc[np.arange(12084,14599)]["CLOSE"]

#2010 - 2017
ten_2_2017 = data1.iloc[np.arange(14599,16612)]["CLOSE"]

#Use a boxplot to visualize changes in Close Price Distribution over time.
names = ['1950 - 1960', '1960 - 1970', '1970 - 1980',
         '1980 - 1990', '1990 - 2000',"2000 - 2010", "2010 - 2017"]
decades = [fifty_2_sixty, sixty_2_seventy,seventy_2_eighty,eighty_2_ninety,ninety_2_00,OO_2_2010,ten_2_2017]

colors = colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00', "#E79F00","#F0D442"]

plt.figure(figsize=(15,9))

plt.boxplot(decades, labels=names,patch_artist=True )
plt.title("How has Close Price Changed by Decade?")


