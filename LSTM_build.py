#Build custom LSTM model
def build_LSTM(X_trn, rnn_units_short,rnn_units_long):
    lstm = tf.keras.Sequential([
    tf.keras.layers.Dense(X_trn.shape[1], activation = "sigmoid", input_shape=(None, X_trn.shape[2])),
    tf.keras.layers.LSTM(rnn_units_long, return_sequences=True, stateful=False, recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(2, activation = "softmax"),
    tf.keras.layers.LSTM(rnn_units_short, return_sequences=False, stateful=False, recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(1,input_shape = (None,1))
  ])
    return lstm
   
#Create an instance of the model
model = build_LSTM(
  X_trn,  
  rnn_units_short=14, #This is meant to represent two weeks prior stock market days
  rnn_units_long = 90) #This is meant to represent the past quarter of stock data
 
#Examine Model Architecture
model.summary() 

#Compile the model
model.compile(optimizer='adam', loss="mean_squared_error") #Compile Model
