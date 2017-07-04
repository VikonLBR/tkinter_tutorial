import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt



#create data
x_data = np.random.rand(100).astype('float32')*10
y_data = 2 * x_data + 0.3
# print(x_data)
# plt.scatter(x_data, y_data, s=x_data, marker="x")
# plt.axis([0, 13, 0, 25])
# plt.show()

###create tensorflow structure###
Weights = tf.Variable(tf.random_uniform([1], -3.0, 3.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))
    #建立优化器
learning_rate = 0.01
#always<1
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
    #建立训练器
train = optimizer.minimize(loss)
    #初始化
init = tf.initialize_all_variables()

###create tensorflow structure###


#激活init
session = tf.Session()
session.run(init)


for step in range(1000):
    session.run(train)
    if step % 100 == 0:
        print(step, session.run(Weights), session.run(biases))
        ss = float(session.run(Weights))
        bi = float(session.run(biases))
        plt.scatter(x_data, y_data, marker='x')
        plt.plot(x_data, ss*x_data+bi)
        plt.show()