#if not already installed, run below
  # if inside a jupyter notebook as I was: !pip install -q tf-nightly-2.0-preview
  # command line: pip install -q tf-nightly-2.0-preview


# Load the TensorBoard notebook extension
%load_ext tensorboard.notebook

logdir = os.path.join("logs", dt.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)

#Call tensorboard to watch model train and understand its architecture better
%tensorboard --logdir logs

#Train the model
history = model.fit(X_trn,y_trn, epochs=1000,batch_size = 4153,validation_split = 0.2, callbacks=[tensorboard_callback], verbose = 0)

#Visualize the training
plt.plot(history.history["loss"])

#Predict and Evaluate Predictions
preds = model.predict(X_tst)
plt.plot(preds, label = "Predicted")
plt.plot(y_tst, label = "Actual")
plt.legend()
plt.show()
