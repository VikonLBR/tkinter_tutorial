import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#添加神经层
def add_layer(inputs, input_size, output_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([input_size, output_size]))
    biases = tf.Variable(tf.zeros([1, output_size])+0.1)#推荐的biases不为零
    Wx_plus_b = tf.matmul(inputs, Weights)+biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return  outputs


x_data = np.linspace(-1, 1, 300)[:, np.newaxis] #300行， 只有一个输入单元，算作只有一个输入神经元
"""
输入层只有一个神经元
中间隐藏层假设有10个神经元
输出只有一个y_data，所以输出层也只有一个输出神经元


"""

noises = np.random.normal(0, 0.05, x_data.shape)

y_data = np.square(x_data) - 0.5 + noises

# plt.scatter(x_data, y_data, marker='x')
#
# plt.show()


#for train step


#只有一个输入神经元，一个输出神经元，故都为1,None代表无论给多少个例子都ok
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])




#inputlayer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

#output layer
prediction = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                     reduction_indices=[1]))


#start training
learning_rate = 0.1
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:#Session后面需要加括号

    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    for i in range(1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))





