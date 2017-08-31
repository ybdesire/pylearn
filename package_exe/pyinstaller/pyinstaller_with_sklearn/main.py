from sklearn.linear_model import SGDClassifier


x_train = []
y_train = []
with open('train.csv', 'r') as fr:
    for line in fr:
        xs = line.split(',')
        x = [float(m) for m in xs]
        x_train.append(x[:len(x)-1])
        y_train.append(x[-1])


x_test = []
with open('test.csv', 'r') as fr:
    for line in fr:
        xs = line.split(',')
        x = [float(m) for m in xs]
        x_test.append(x)


model = SGDClassifier(random_state=6)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)


with open('result.csv', 'w') as fw:
    for y in y_pred:
        fw.write('{0}\n'.format(int(y)))

