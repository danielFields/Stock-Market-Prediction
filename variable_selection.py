num_NA = pd.DataFrame()
num_NA["Num_NA"] = data1.isnull().sum(axis = 0)
num_NA["Proportion_NA"] = np.round((num_NA["Num_NA"]*100)/len(data1["CLOSE"]),3)
num_NA.query("Proportion_NA > 0").sort_values("Proportion_NA", ascending = False)

print("So, there are a total of ",len(num_NA.query("Num_NA > 0").index), "variables with missing observations.")

#implementing 2% cutoff: if > 2% of the observations of a variable are missing, then that variable will be excluded from the analysis
within_tolerance = num_NA.query("Proportion_NA < 2 & Proportion_NA > 0")

#wihtin NA tolerance are: `RELINF`, `DVY`, and `CATY` variables.

#replace missing values with the mean of each variable of which is within tolerance

data1["DVY"][data1["DVY"].isnull()] = np.mean(data1["DVY"]) #Replace missing values of DVY with mean of DVY

data1["CATY"][data1["CATY"].isnull()] = np.mean(data1["CATY"]) #Replace missing values of CATY with mean of CATY

data1["RELINF"][data1["RELINF"].isnull()] = np.mean(data1["RELINF"]) #Replace missing of RELINF values with mean of RELINF

#Verify that variables selected are all now complete
num_NA2 = pd.DataFrame()
num_NA2["Num_NA"] = data1.isnull().sum(axis = 0)
num_NA2["Proportion_NA"] = np.round((num_NA2["Num_NA"]*100)/len(data1["CLOSE"]),3)
num_NA2.query("Proportion_NA < 2").sort_values("Proportion_NA", ascending = False)

#Variable Selection
data2 = data1[num_NA2.query("Proportion_NA < 2").index].drop("Date", axis = 1) #Get variables we will be using using 2% NA tolerance

#Examine design matrix for modeling
data2.info()

#Split data into design matrix and target
X = data2.drop(["CLOSE"], axis = 1)
y = data2["CLOSE"]

#Scale Design Matrix
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

#Split design matrix and target into training and testing splits and reshape for modeling
X_trn = X.head(int(0.8*X.shape[0])).values.reshape(int(0.8*X.shape[0]),X.shape[1],1)
X_tst = X.tail(int(0.2*X.shape[0])).values.reshape(int(0.2*X.shape[0]),X.shape[1],1)

y_trn = y.head(int(0.8*X.shape[0])).values
y_tst = y.tail(int(0.2*X.shape[0])).values
