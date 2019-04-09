# Load Data
data = pd.read_csv("dataset.csv")

#Drop columns with all missing values
data1 = data.drop(["ASPFWR5","sentiment1","sentiment2","sentiment3","Hulbert.sentiment"], axis = 1)

#Relabel indexes
data1 = data1.reset_index(drop = True)

#Format Dates
data1 = data1.rename(columns = {"Unnamed: 0":"Date"})

#Examine Data
data1.head()

#Exploratory Questions and Answers
print("How many days of trading does this dataset encompass?")
print(len(data1["Date"]), "Days" )


print("What was the highest close price and when did it occur?")
print(np.max(data1["CLOSE"]), "on ", data1["Date"][data1["CLOSE"] == np.max(data1["CLOSE"])].values)

print("What was the lowest close price and when did it occur?")
print(np.min(data1["CLOSE"]), "on ", data1["Date"][data1["CLOSE"] == np.min(data1["CLOSE"])].values)

