import pickle
import csv_writer

data = open('x.txt', 'rb')
x = pickle.load(data)
data.close()

# for el in x:
#     print(el)

data = open('y.txt', 'rb')
y = pickle.load(data)
data.close()

# print(y)
# y_true = 0
# y_false = 0
# for el in y:
#     if el == 1:
#         y_true += 1
# y_false = len(y)-y_true
# print(y_true, y_false)

y_array = []
for el in y:
    y_array.append([el])

csv_writer.csv_writer(x, 'x.csv')

