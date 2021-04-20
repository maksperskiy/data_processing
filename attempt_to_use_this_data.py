import os
import numpy as np
import re
from tensorflow.keras.layers import Dense, LSTM, Input, Dropout, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer, text_to_word_sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle


data = open('x.txt', 'rb')
x = pickle.load(data)
data.close()

data = open('y.txt', 'rb')
y = pickle.load(data)
data.close()


x_train = np.asarray(x[:80])
print("len x_train - ", len(x_train))
x_test = np.asarray(x[80:])
print("len x_test - ", len(x_test))
print(x_train.shape, '\n')
print(x_train, '\n')
print(x_test)

y_train = np.asarray(y[:80]).reshape(len(y[:80]), -1)
print("len y_train - ", len(y_train))
y_test = np.asarray(y[80:]).reshape(len(y[80:]), -1)
print("len y_test - ", len(y_test))
print(y_train.shape, '\n')
print(y_train, '\n')
print(y_test)


model = Sequential()
model.add(Embedding(40000, 128, input_length = 300))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(64))
model.add(Dense(1, activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=Adam(0.0001))

history = model.fit(x_train, y_train, batch_size=32, epochs=60)

num = 0
res = model.predict(x_test[num])
print(y_test[num])
print(res)
