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


y_pred = []

for x in x_test:
    min_v = 1000000
    min_index = 0
    for i in range(len(x_train)):
        xx = x_train[i]
        d = 0
        for j in range(len(xx)):
            d += abs(xx[j]-x[j])
            
        if(d<min_v):
            min_v = d
            min_index = i
    y_pred.append(y_train[min_index])
    
    
with open('result.csv', 'w') as fw:
    for y in y_pred:
        fw.write('{0}\n'.format(int(y)))

